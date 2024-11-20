# Quantum Safe CA

Experimentations with _quantum safe_ algorithms and _X509_ certificates.

**Dependencies:**

Please install [oqsprovider](https://github.com/open-quantum-safe/oqs-provider) according to their documentation and configure _oqs-provider_ globally to your _OpenSSL_.

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
