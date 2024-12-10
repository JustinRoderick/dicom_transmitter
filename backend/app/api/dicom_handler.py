import requests
from config import ORTHANC_URL

PARAM_STUDIES_EXPAND = "studies?requested-tags=AccessionNumber&expand"
PARAM_PATIENTS_EXPAND = "patients?requested-tags=PatientID&expand"

def query_orthanc_id_by_accession (accession_number: str):
    url = f"{ORTHANC_URL}/tools/find"
    req_body = {
        "Expand": False,
        "Level": "Study",
        "Query": {"AccessionNumber": accession_number}
    }
    response = requests.post(url, json=req_body)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
        return {"error": "No matching studies found"}

    response_data = response.json()

    matches = []
    for study in response_data:
        matches.append(study)
    return {"matching_ids": matches}

def query_patient_id_by_mrn (mrn: str):
    url = f"{ORTHANC_URL}/tools/find"
    req_body = {
        "Expand": False,
        "Level": "Patient",
        "Query": {"PatientID": mrn}
    }
    response = requests.post(url, json=req_body)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
        return {"error": "No matching patients found"}

    response_data = response.json()

    matches = []
    for patient in response_data:
        matches.append(patient)
    return {"matching_ids": matches}

def query_mrn_accession_filter (accession_number: str, mrn: str):
    url = f"{ORTHANC_URL}/tools/find"
    req_body = {
        "Expand": True,
        "Level": "Study",
        "Query": {"AccessionNumber": accession_number}
    }

    response = requests.post(url, json=req_body)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
        return {"error": "No matching studies found"}

    response_data = response.json()

    matches = []
    for study in response_data:
        patient_tags = study["PatientMainDicomTags"]
        if "PatientID" in patient_tags and patient_tags["PatientID"] == mrn:
            matches.append(study);

    return matches

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
