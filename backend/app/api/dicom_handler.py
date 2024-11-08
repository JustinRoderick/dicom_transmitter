import requests
from config import ORTHANC_URL

def retrieve_dicom (accession_number: str):
    # Need to find correct URL for Orthanc
    url = f"{ORTHANC_URL}/instances/{accession_number}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "DICOM not found"}
    return response.content

def query_orthanc_id_by_accession (accession_number: str):
    return "0"

def query_patient_resource_by_id (orthanc_id: str):
    return {"ID": "0", "Type": "PatientPlaceholder"}

def query_study_resource_by_id (orthanc_id: str):
    return {"ID": "ABC", "Type": "StudyPlaceholder"}
