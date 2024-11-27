from fastapi.testclient import TestClient
import pytest
from qsca.main import app


client = TestClient(app)


@pytest.mark.parametrize("path", ["server", "iota", "iotb"])
def test_get_server_certificate_chain(path):
    response = client.get(f"/cacerts/{path}")

    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/x-pem-file"
