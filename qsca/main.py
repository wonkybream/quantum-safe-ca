from fastapi import FastAPI, Response, status
from fastapi.responses import FileResponse

from qsca.commands import pem_to_pkcs7
from qsca.configuration import CERTIFICATE_CHAINS


app = FastAPI()


@app.get(
    "/.well-known/est/{chain_label}/cacerts",
    responses={
        200: {
            "content": {"application/pkcs7-mime": {}},
            "description": "A certs-only CMC Simple PKI Response",
        },
        404: {
            "content": {"text/plain": {}},
            "description": "Certificate chain not found",
        },
        422: {
            "content": {"text/plain": {}},
            "description": "Unprocessable Content",
        },
    },
    response_class=Response,
    name="CA Certificates Request",
    tags=["Distribution of CA"],
)
async def get_ca_certificates(chain_label: str):
    """
    Returns the PKCS#7 certificate chain for the given label.
    """
    if chain_label not in CERTIFICATE_CHAINS.keys():
        return Response(
            status_code=status.HTTP_404_NOT_FOUND,
            content="Certificate chain not found",
            media_type="text/plain",
        )

    pem_file = CERTIFICATE_CHAINS[chain_label]
    pkcs7_file = pem_file.with_suffix(".p7b")

    if not pkcs7_file.exists() or pem_file.stat().st_mtime > pkcs7_file.stat().st_mtime:
        pem_to_pkcs7(pem_file, pkcs7_file)

    return FileResponse(
        pkcs7_file,
        media_type="application/pkcs7-mime",
        filename=f"{chain_label}_chain.p7b",
    )

    # with open(pkcs7_file, "rb") as f:
    #     pkcs7_data = f.read()
    #     base64_data = base64.b64encode(pkcs7_data).decode("ascii")

    # return Response(
    #     content=base64_data,
    #     media_type="application/pkcs7-mime",
    #     headers={"Content-Transfer-Encoding": "base64"}
    # )
