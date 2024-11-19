import os
from dotenv import load_dotenv

load_dotenv()

ORTHANC_URL = "http://demo:demo@" + os.getenv("ORTHANC_URL")
HAPI_FHIR_URL = os.getenv("HAPI_FHIR_URL")
