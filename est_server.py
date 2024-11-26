from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

ROOT_DIR = Path("ca")
SERVER_CA_PATH = ROOT_DIR / "server"
IOT_A_CA_PATH = ROOT_DIR / "iot"
IOT_B_CA_PATH = ROOT_DIR / "iot"

@app.get("/cacerts/server")
async def get_server_cert_tree():
    """
    Returns server certificate chain
    """
    file_path = SERVER_CA_PATH / "chain_a.pem"
    return FileResponse(file_path, media_type="application/x-pem-file", filename="server_chain.pem")

@app.get("/cacerts/iota")
async def get_iota_cert_tree():
    """
    Returns IoT A certificate chain
    """
    file_path = IOT_A_CA_PATH / "chain_a.pem"
    return FileResponse(file_path, media_type="application/x-pem-file", filename="iot_a_chain.pem")

@app.get("/cacerts/iotb")
async def get_iotb_cert_tree():
    """
    Return IoT B certificate chain
    """
    file_path = IOT_B_CA_PATH / "chain_b.pem"
    return FileResponse(file_path, media_type="application/x-pem-file", filename="iot_b_chain.pem")
