import requests
from config import ORTHANC_URL

PARAM_STUDIES_EXPAND = "studies?requested-tags=AccessionNumber&expand"

def query_orthanc_id_by_accession (accession_number: str):
    url = f"{ORTHANC_URL}/{PARAM_STUDIES_EXPAND}"
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
        return {"error": response.status_code}

    response_data = response.json()

    matches = []
    for study in response_data:
        tags = study['MainDicomTags']
        if 'AccessionNumber' in tags and tags['AccessionNumber'] == accession_number:
            matches.append(study['ID'])
    return {"matching_ids": matches}

def query_patient_resource_by_id (orthanc_id: str):
    return {"ID": "0", "Type": "PatientPlaceholder"}

def query_study_resource_by_id (orthanc_id: str):
    return {"ID": "ABC", "Type": "StudyPlaceholder"}
