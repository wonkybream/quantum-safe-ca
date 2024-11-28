import os
from pathlib import Path
import subprocess

from qsca.configuration import CERTIFICATE_VALIDITY_DAYS


def generate_key(algorithm: str, key_file: Path):
    """
    Generate a private key using OpenSSL.
    """
    command = ["openssl", "genpkey", "-algorithm", algorithm, "-out", key_file]
    subprocess.run(command, check=True, env=os.environ.copy())


def sign_file(data_file: Path, key_file: Path, signed_file: Path):
    """
    Sign the input data (which must be a hash) and output the signed result.
    """
    command = [
        "openssl",
        "pkeyutl",
        "-sign",
        "-in",
        data_file,
        "-inkey",
        key_file,
        "-out",
        signed_file,
    ]
    subprocess.run(command, check=True, env=os.environ.copy())


def verify_signature(data_file: Path, key_file: Path, signed_file: Path):
    """
    Verify the input data (which must be a hash) against the signature file and indicate if the verification succeeded or failed.
    """
    command = [
        "openssl",
        "pkeyutl",
        "-verify",
        "-in",
        data_file,
        "-inkey",
        key_file,
        "-sigfile",
        signed_file,
    ]
    try:
        subprocess.run(command, check=True, env=os.environ.copy())
        return True
    except subprocess.CalledProcessError:
        return False


def sign_csr(csr_file: Path, key_file: Path, certificate_file: Path, output_file: Path):
    """
    Signs a CSR and generates a certificate.
    """
    command = [
        "openssl",
        "x509",
        "-req",
        "-in",
        csr_file,
        "-CA",
        certificate_file,
        "-CAkey",
        key_file,
        "-CAcreateserial",
        "-out",
        output_file,
        "-days",
        CERTIFICATE_VALIDITY_DAYS,
    ]
    subprocess.run(command, check=True, env=os.environ.copy())


def pem_to_pkcs7(pem_file: Path, output_file: Path):
    """
    Converts PEM certificates to PKCS#7 format using OpenSSL.
    """
    command = [
        "openssl",
        "crl2pkcs7",
        "-certfile",
        pem_file,
        "-out",
        output_file,
        "-nocrl",
    ]
    subprocess.run(command, check=True, env=os.environ.copy())
