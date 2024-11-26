import os
from pathlib import Path
import subprocess


def generate_key(algorithm: str, key_file: Path):
    """
    Generate a private key using OpenSSL
    """
    command = ["openssl", "genpkey", "-algorithm", algorithm, "-out", key_file]
    subprocess.run(command, check=True, env=os.environ.copy())


def sign_file(data_file: Path, key_file: Path, signed_file: Path):
    """
    Sign the input data (which must be a hash) and output the signed result
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
    Verify the input data (which must be a hash) against the signature file and indicate if the verification succeeded or failed
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
