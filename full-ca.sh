#!/usr/bin/env bash

# Test creation and verification of two certificate chains using oqsprovider for alg $1

export DYLD_LIBRARY_PATH="/Usr/local/lib"

if [ $# -ne 1 ]; then
    echo "Usage: $0 <algorithm name>. Exiting."
    exit 1
fi

echo "Using '$1' algorithm..."

CA_NAME=$(grep '^.\{6\}$' /usr/share/dict/words | sort -R | head -1)

if [ -d "$CA_NAME" ]; then
    echo "Directory $CA_NAME already exists. Exiting."
    exit 1
fi

mkdir $CA_NAME && cd $CA_NAME

# Root certificate
openssl genpkey -algorithm $1 -out root_key.pem
openssl req -x509 -new -key root_key.pem -days 3650 -out root_cert.pem -subj "/CN=Root Certificate"
echo "Root certificate created successfully"

# Intermediate A and B certificates
openssl genpkey -algorithm $1 -out intermediate_a_key.pem
openssl genpkey -algorithm $1 -out intermediate_b_key.pem

openssl req -new -key intermediate_a_key.pem -out intermediate_a.csr -subj "/CN=Intermediate A"
openssl req -new -key intermediate_b_key.pem -out intermediate_b.csr -subj "/CN=Intermediate B"

openssl x509 -req -in intermediate_a.csr -CA root_cert.pem -CAkey root_key.pem -CAcreateserial -days 1825 -out intermediate_a_cert.pem
openssl x509 -req -in intermediate_b.csr -CA root_cert.pem -CAkey root_key.pem -CAcreateserial -days 1825 -out intermediate_b_cert.pem
echo "Intermediate A and B certificates created successfully"

# Combine chains
cat intermediate_a_cert.pem root_cert.pem > chain_a.pem
cat intermediate_b_cert.pem root_cert.pem > chain_b.pem

openssl verify -CAfile root_cert.pem chain_a.pem
openssl verify -CAfile root_cert.pem chain_b.pem

echo "Done, both chains are located in folder '$CA_NAME'"
