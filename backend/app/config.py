import os
from dotenv import load_dotenv

load_dotenv()

# FIXCONFIG
ORTHANC_URL = "http://demo:demo@backend-orthanc:8042"
HAPI_FHIR_URL = os.getenv("HAPI_FHIR_URL")
