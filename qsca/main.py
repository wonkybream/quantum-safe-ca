from fastapi import FastAPI
from fastapi.responses import FileResponse

from qsca.configuration import RESOURCES_DIR

app = FastAPI()

CA_DIR = RESOURCES_DIR
SERVER_CA_PATH = CA_DIR / "server_chain"
IOT_A_CA_PATH = CA_DIR / "iot_chain"
IOT_B_CA_PATH = CA_DIR / "iot_chain"


@app.get("/cacerts/server")
async def get_server_cert_tree():
    """
    Returns server certificate chain
    """
    file_path = SERVER_CA_PATH / "chain_a.pem"
    return FileResponse(
        file_path, media_type="application/x-pem-file", filename="server_chain.pem"
    )


@app.get("/cacerts/iota")
async def get_iota_cert_tree():
    """
    Returns IoT A certificate chain
    """
    file_path = IOT_A_CA_PATH / "chain_a.pem"
    return FileResponse(
        file_path, media_type="application/x-pem-file", filename="iot_a_chain.pem"
    )


@app.get("/cacerts/iotb")
async def get_iotb_cert_tree():
    """
    Return IoT B certificate chain
    """
    file_path = IOT_B_CA_PATH / "chain_b.pem"
    return FileResponse(
        file_path, media_type="application/x-pem-file", filename="iot_b_chain.pem"
    )
