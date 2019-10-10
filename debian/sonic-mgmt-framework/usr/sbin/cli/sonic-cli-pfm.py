#!/usr/bin/python
###########################################################################
#
# Copyright 2019 Dell, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###########################################################################

import sys
import time
import json
import ast
import openconfig_platform_client
from rpipe_utils import pipestr
from openconfig_platform_client.rest import ApiException
from scripts.render_cli import show_cli_output


import urllib3
urllib3.disable_warnings()

blocked_fields = {'parent':0, 'used_power':0, 'allocated_power':0, 'temperature':0}
plugins = dict()

def filter_json_value(value):
    for key,val in value.items():
        if key in blocked_fields:
            del value[key]
        else:
	    temp = key.split('_')
	    alt_key = ''
	    for i in temp:
		alt_key = alt_key + i.capitalize() + ' '
	    value[alt_key]=value.pop(key)

    return value

def register(func):
    """Register sdk client method as a plug-in"""
    plugins[func.__name__] = func
    return func


def call_method(name, args):
    method = plugins[name]
    return method(args)

def generate_body(func, args):
    body = None
    # Get the rules of all ACL table entries.

    if func.__name__ == 'get_openconfig_platform_components':
        keypath = []

    else:
       body = {}

    return keypath,body


def run(func, args):
    c = openconfig_platform_client.Configuration()
    c.verify_ssl = False
    aa = openconfig_platform_client.OpenconfigPlatformApi(api_client=openconfig_platform_client.ApiClient(configuration=c))

    # create a body block
    keypath, body = generate_body(func, args)

    try:
        if body is not None:
           api_response = getattr(aa,func.__name__)(*keypath, body=body)

        else :
           api_response = getattr(aa,func.__name__)(*keypath)
     
        if api_response is None:
            print ("Success")
        else:
            api_response = aa.api_client.sanitize_for_serialization(api_response)
            value =  api_response['openconfig-platform:components']['component'][0]['state']
	    if value is None:
                return
	    if 'oper-status' in value:
		temp = value['oper-status'].split(':')
		if temp[len(temp) - 1] is not None:
	            value['oper-status'] = temp[len(temp) - 1]
            show_cli_output(sys.argv[2],filter_json_value(value))

    except ApiException as e:
        if e.body != "":
            body = json.loads(e.body)
            if "ietf-restconf:errors" in body:
                 err = body["ietf-restconf:errors"]
                 if "error" in err:
                     errList = err["error"]

                     errDict = {}
                     for dict in errList:
                         for k, v in dict.iteritems():
                              errDict[k] = v

                     if "error-message" in errDict:
                         print "%Error: " + errDict["error-message"]
                         return
                     print "%Error: Application Failure"
                     return
            print "%Error: Application Failure"
        else:
            print "Failed"

if __name__ == '__main__':

    pipestr().write(sys.argv)
    #pdb.set_trace()
    func = eval(sys.argv[1], globals(), openconfig_platform_client.OpenconfigPlatformApi.__dict__)
    run(func, sys.argv[2:])

