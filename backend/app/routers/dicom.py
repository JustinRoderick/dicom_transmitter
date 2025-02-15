from fastapi import APIRouter
from pydantic import BaseModel
from api.dicom_handler import *

class Filter(BaseModel):
    accession_number: str
    mrn: str

router = APIRouter()

@router.get("/accession/{accession_number}")
async def get_orthanc_id(accession_number: str):
    return query_orthanc_id_by_accession(accession_number)

@router.get("/mrn/{mrn}")
async def get_patient_id(mrn: str):
    return query_patient_id_by_mrn(mrn)

@router.get("/{orthanc_id}")
async def get_study_resource(orthanc_id: str):
    return query_study_by_id(orthanc_id)

@router.post("/find")
async def find_study(query: Filter):
    return query_mrn_accession_filter(query.accession_number, query.mrn)

@router.get("/{orthanc_id}/patient")
async def get_study_patient(orthanc_id: str):
    res = query_patient_by_study_id(orthanc_id)
    if "error" in res:
        return res
    return {"patientinfo": res}




