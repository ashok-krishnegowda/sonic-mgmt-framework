#!/bin/sh

#****************************************
rootcert() {
	ROOTCERTDIR="/host/cli-ca"
	if [ ! -d "${ROOTCERTDIR}" ]; then
		echo "Generating root certificates"

		ca_conf="$(mktemp -t ca.conf.XXXXXXXXXX)"
		cat <<-EOF >>"${ca_conf}"
# The main section is named req because the command we are using is req
# (openssl req ...)
[ req ]
# This specifies the default key size in bits. If not specified then 512 is
# used. It is used if the -new option is used. It can be overridden by using
# the -newkey option.
default_bits = 2048
# If this is set to no then if a private key is generated it is not encrypted.
# This is equivalent to the -nodes command line option. For compatibility
# encrypt_rsa_key is an equivalent option.
encrypt_key = no
# This option specifies the digest algorithm to use. Possible values include
# md5 sha1 mdc2. If not present then MD5 is used. This option can be overridden
# on the command line.
default_md = sha256
# if set to the value no this disables prompting of certificate fields and just
# takes values from the config file directly. It also changes the expected
# format of the distinguished_name and attributes sections.
prompt = no
# if set to the value yes then field values to be interpreted as UTF8 strings,
# by default they are interpreted as ASCII. This means that the field values,
# whether prompted from a terminal or obtained from a configuration file, must
# be valid UTF8 strings.
utf8 = yes
# This specifies the section containing the distinguished name fields to
# prompt for when generating a certificate or certificate request.
distinguished_name = my_req_distinguished_name
# this specifies the configuration file section containing a list of extensions
# to add to the certificate request. It can be overridden by the -reqexts
# command line switch. See the x509v3_config(5) manual page for details of the
# extension section format.
x509_extensions        = v3_ca
[v3_ca]
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid,issuer
basicConstraints       = CA:TRUE, pathlen:0
#keyUsage               = digitalSignature, nonRepudiation
subjectAltName         = email:copy,email:support@dell.com
issuerAltName          = issuer:copy
[my_req_distinguished_name]
commonName  = localhost
countryName = US
		EOF

		mkdir -p ${ROOTCERTDIR}
		openssl genrsa -out ${ROOTCERTDIR}/key.pem 2048
		openssl req -new -x509 -key ${ROOTCERTDIR}/key.pem -out ${ROOTCERTDIR}/cert.pem -config "${ca_conf}" -days 3650
	fi
}

#****************************************
certgen() {
	user=$1
	USRHOME=$(getent passwd "${user}" | cut -d: -f6)
	if [ -d "${USRHOME}" ]; then # First make sure user's home directory exists
		CERTDIR="${USRHOME}/.cert"
		if [ ! -d "${CERTDIR}" ]; then
			echo "Generating ${user} certificates"
			/usr/bin/certgen "${user}"
		fi
	fi
}

rootcert
certgen admin
