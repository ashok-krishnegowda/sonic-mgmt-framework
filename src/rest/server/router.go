////////////////////////////////////////////////////////////////////////////////
//                                                                            //
//  Copyright 2019 Broadcom. The term Broadcom refers to Broadcom Inc. and/or //
//  its subsidiaries.                                                         //
//                                                                            //
//  Licensed under the Apache License, Version 2.0 (the "License");           //
//  you may not use this file except in compliance with the License.          //
//  You may obtain a copy of the License at                                   //
//                                                                            //
//     http://www.apache.org/licenses/LICENSE-2.0                             //
//                                                                            //
//  Unless required by applicable law or agreed to in writing, software       //
//  distributed under the License is distributed on an "AS IS" BASIS,         //
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  //
//  See the License for the specific language governing permissions and       //
//  limitations under the License.                                            //
//                                                                            //
////////////////////////////////////////////////////////////////////////////////

package server

import (
    "net/http"
    "strings"
    "time"
    "github.com/golang/glog"
    "github.com/gorilla/mux"
)

// Root directory for UI files
var swaggerUIDir = "./ui"

// SetUIDirectory functions sets directiry where Swagger UI
// resources are maintained.
func SetUIDirectory(directory string) {
	swaggerUIDir = directory
}

// Route registration information
type Route struct {
	Name    string
	Method  string
	Pattern string
	Handler http.HandlerFunc
}

// Collection of all routes
var allRoutes []Route

// AddRoute appends specified routes to the routes collection.
// Called by init functions of swagger generated router.go files.
func AddRoute(name, method, pattern string, handler http.HandlerFunc) {
	route := Route{
		Name:    name,
		Method:  strings.ToUpper(method),
		Pattern: pattern,
		Handler: handler,
	}

	allRoutes = append(allRoutes, route)
}

// NewRouter function returns a new http router instance. Collects
// route information from swagger-codegen generated code and makes a
// github.com/gorilla/mux router object.
func NewRouter() *mux.Router {
	router := mux.NewRouter().StrictSlash(true).UseEncodedPath()
	allPaths := make(map[string]bool)

	glog.Infof("Server has %d paths", len(allRoutes))

	// Collect swagger generated route information
	for _, route := range allRoutes {
		allPaths[route.Pattern] = true
		handler := withMiddleware(route.Handler, route.Name)

		glog.V(2).Infof(
			"Adding %s, %s %s",
			route.Name, route.Method, route.Pattern)

		router.
			Methods(route.Method).
			Path(route.Pattern).
			Name(route.Name).
			Handler(handler)
	}

	// Register common OPTIONS handler for every path template
	oh := withMiddleware(http.HandlerFunc(commonOptionsHandler), "optionsHandler")
	for p := range allPaths {
		router.Methods("OPTIONS").Path(p).Handler(oh)
	}

	// Documentation and test UI
	uiHandler := http.StripPrefix("/ui/", http.FileServer(http.Dir(swaggerUIDir)))
	router.Methods("GET").PathPrefix("/ui/").Handler(uiHandler)

	// Redirect "/ui" to "/ui/index.html"
	router.Methods("GET").Path("/ui").
		Handler(http.RedirectHandler("/ui/index.html", 301))

	if ClientAuth.Enabled("jwt") {
		router.Methods("POST").Path("/authenticate").Handler(http.HandlerFunc(Authenticate))
		router.Methods("POST").Path("/refresh").Handler(http.HandlerFunc(Refresh))
	}

	// To download yang models
	ydirHandler := http.FileServer(http.Dir(translib.GetYangPath()))
	router.Methods("GET").PathPrefix("/models/yang/").
		Handler(http.StripPrefix("/models/yang/", ydirHandler))

	return router
}

// commonOptionsHandler is the common HTTP OPTIONS method handler
// for all path based routes. Resolves allowed methods for current
// path template by traversing allRoutes cache.
func commonOptionsHandler(w http.ResponseWriter, r *http.Request) {
	var methods []string
	var hasPatch bool
	t, _ := mux.CurrentRoute(r).GetPathTemplate()

	// Collect allowed method names
	for _, r := range allRoutes {
		if r.Pattern == t {
			methods = append(methods, r.Method)
			if r.Method == "PATCH" {
				hasPatch = true
			}
		}
	}

	// "Allow" header
	if len(methods) != 0 {
		methods = append(methods, "OPTIONS") // OPTIONS will not be part of allRoutes
		sort.Strings(methods)
		w.Header().Set("Allow", strings.Join(methods, ", "))
	}

	// "Accept-Patch" header for RESTCONF data paths
	if hasPatch && strings.HasPrefix(t, restconfDataPathPrefix) {
		w.Header().Set("Accept-Patch", mimeYangDataJSON)
	}
}

// loggingMiddleware returns a handler which times and logs the request.
// It should be the top handler in the middleware chain.
func loggingMiddleware(inner http.Handler, name string) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		rc, r := GetContext(r)
		rc.Name = name

		glog.Infof("[%s] Recevied %s request from %s", rc.ID, name, r.RemoteAddr)

		start := time.Now()

		inner.ServeHTTP(w, r)

		glog.Infof("[%s] %s took %s", rc.ID, name, time.Since(start))
	})
}

// withMiddleware function prepares the default middleware chain for
// REST APIs.
func withMiddleware(h http.Handler, name string) http.Handler {
	if ClientAuth.Any() {
		h = authMiddleware(h)
	}

	return loggingMiddleware(h, name)
}

// authMiddleware function creates a middleware for request
// authentication and authorization. This middleware will return
// 401 response if authentication fails and 403 if authorization
// fails.
func authMiddleware(inner http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		rc, r := GetContext(r)
		var err error
		success := false
		if ClientAuth.Enabled("password") {
			err = BasicAuthenAndAuthor(r, rc)
			if err == nil {
				success = true
			}
		}
		if !success && ClientAuth.Enabled("jwt") {
			_, err = JwtAuthenAndAuthor(r, rc)
			if err == nil {
				success = true
			}
		}
		if !success && ClientAuth.Enabled("cert") {
			err = ClientCertAuthenAndAuthor(r, rc)
			if err == nil {
				success = true
			}
		}

		if !success {
			status, data, ctype := prepareErrorResponse(err, r)
			w.Header().Set("Content-Type", ctype)
			w.WriteHeader(status)
			w.Write(data)
		} else {
			inner.ServeHTTP(w, r)
		}
	})
}
