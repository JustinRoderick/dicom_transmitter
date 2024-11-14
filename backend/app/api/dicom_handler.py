import requests
from config import ORTHANC_URL

PARAM_STUDIES_EXPAND = "studies?requested-tags=AccessionNumber&expand"

def query_orthanc_id_by_accession (accession_number: str):
    url = f"{ORTHANC_URL}/{PARAM_STUDIES_EXPAND}"
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
        return {"error": "No matching studies found"}

    response_data = response.json()

    matches = []
    for study in response_data:
        tags = study["MainDicomTags"]
        if "AccessionNumber" in tags and tags["AccessionNumber"] == accession_number:
            matches.append(study["ID"])
    return {"matching_ids": matches}

def query_study_by_id (orthanc_id: str):
    url = f"{ORTHANC_URL}/studies/{orthanc_id}"
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
        return {"error": "Study not found"}

    return response.json()

def query_patient_by_study_id (orthanc_id: str):
    url = f"{ORTHANC_URL}/studies/{orthanc_id}/patient"
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
        return {"error": "Patient not found"}

    response_data = response.json()
    tags = response_data['MainDicomTags']
    
    resname = "N/A"
    resbirth = "N/A"
    if "PatientName" in tags:
        resname = tags["PatientName"]
    if "PatientBirthDate" in tags: 
        resbirth = tags["PatientBirthDate"]
    
    return {"name": resname, "birthdate": resbirth}
