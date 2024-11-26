from qsca.utils.commands import generate_key, sign_file, verify_signature


def test_sign_and_verify_using_dilithium3(tmp_path):
    key_file = tmp_path / "key.pem"
    data_file = tmp_path / "hello.txt"
    signed_file = tmp_path / "hello.sig"
    algorithm = "dilithium3"

    with open(data_file, "w") as f:
        f.write("Hello, Quantum Safe World!")
    generate_key(algorithm=algorithm, key_file=key_file)
    sign_file(data_file=data_file, key_file=key_file, signed_file=signed_file)

    verification_result = verify_signature(
        data_file=data_file, key_file=key_file, signed_file=signed_file
    )
    assert verification_result
