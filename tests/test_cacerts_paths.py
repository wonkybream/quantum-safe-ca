from fastapi.testclient import TestClient
import pytest
from qsca.main import app


client = TestClient(app)


@pytest.mark.parametrize("chain_label", ["server", "iot_a", "iot_b"])
def test_get_server_certificate_chain(chain_label):
    response = client.get(f"/.well-known/est/{chain_label}/cacerts")

    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/pkcs7-mime"


def test_get_server_certificate_chain_returns_not_found():
    response = client.get("/.well-known/est/unknown/cacerts")

    assert response.status_code == 404
