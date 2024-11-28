from pathlib import Path


ROOT_DIR = Path().parent
RESOURCES_DIR = ROOT_DIR / "resources"

CERTIFICATE_VALIDITY_DAYS = 365 * 4

SERVER_CA_CERTIFICATE_DIR = RESOURCES_DIR / "server_chain"
IOT_CA_CERTIFICATE_DIR = RESOURCES_DIR / "iot_chain"
CERTIFICATE_CHAINS = {
    "server": SERVER_CA_CERTIFICATE_DIR / "chain_a.pem",
    "iot_a": IOT_CA_CERTIFICATE_DIR / "chain_a.pem",
    "iot_b": IOT_CA_CERTIFICATE_DIR / "chain_b.pem",
}

# ISSUED_CERTIFICATES_PATH = RESOURCES_DIR / "issued_certificates"
