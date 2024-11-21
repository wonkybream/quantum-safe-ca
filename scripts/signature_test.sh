#!/usr/bin/env bash

# Test creation and verification of signature using oqsprovider for alg $1
set -e
cd $(dirname $0) && cd ..

export DYLD_LIBRARY_PATH="/Usr/local/lib"

if [ $# -ne 1 ]; then
    echo "Usage: $0 <algorithm name>. Exiting."
    exit 1
fi

echo "Using '$1' algorithm..."

openssl genpkey -algorithm $1 -out $1_key.pem
echo "Hello World!" > hello.txt
openssl pkeyutl -sign -in hello.txt -inkey $1_key.pem -out hello.sig
openssl pkeyutl -verify -in hello.txt -sigfile hello.sig -inkey $1_key.pem

rm $1_key.pem
rm hello.txt
rm hello.sig
