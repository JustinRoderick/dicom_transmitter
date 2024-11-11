from fastapi import APIRouter
from api.dicom_handler import *

router = APIRouter()

@router.get("/studies/accession/{accession_number}")
async def get_orthanc_id(accession_number: str):
    return {"AccessionNumber": accession_number, 
            "ID": query_orthanc_id_by_accession(accession_number)}

@router.get("/patients/id/{orthanc_id}")
async def get_patient_resource(orthanc_id: str):
        return query_patient_resource_by_id(orthanc_id)

@router.get("/studies/id/{orthanc_id}")
async def get_study_resource(orthanc_id: str):
        return query_study_resource_by_id(orthanc_id)

