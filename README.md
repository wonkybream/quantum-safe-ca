# Quantum Safe CA

Experimentations with _quantum safe_ algorithms and _X509_ certificates.

**Dependencies:**

Please install [_oqsprovider_](https://github.com/open-quantum-safe/oqs-provider) according to their documentation and configure _oqs-provider_ globally to your _OpenSSL_.

Should look something like following.

```shell
openssl list -providers
# Providers:
#   default
#     name: OpenSSL Default Provider
#     version: 3.4.0
#     status: active
#   oqsprovider
#     name: OpenSSL OQS Provider
#     version: 0.7.1-dev
#     status: active
```

## Usage

Providing few different ways of using this tool. There are few scripts just for playing around with certificates. And then there's the _EST server_, which tries to be somewhat [_RFC 7030_](https://datatracker.ietf.org/doc/html/rfc7030) compliant.

**Creating CA**

Creates a certificate chain with two intermediate certificates _A_ and _B_. This also serves as a test whether you have set up the [_oqsprovider_](https://github.com/open-quantum-safe/oqs-provider) correctly

```shell
# Using classical algorithm
./scripts/full_ca.sh ed25519

# Using quantum-safe algorithm
./scripts/full_ca.sh dilithium3
```
