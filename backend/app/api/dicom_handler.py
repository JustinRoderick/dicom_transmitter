import requests
from config import ORTHANC_URL

def retrieve_dicom (accession_number: str):
    # Need to find correct URL for Orthanc
    url = f"{ORTHANC_URL}/instances/{accession_number}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "DICOM not found"}
    return response.content
