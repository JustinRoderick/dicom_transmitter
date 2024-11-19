import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.fhir_handler import create_patient, create_new_patient, construct_patient_resource 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

class PatientRequest(BaseModel):
    patient_id: str
    study_id: str

@router.post("/process-patient-data")
async def process_patient_data(request: PatientRequest):
    try:
        fhir_data = request.patient_id
        dicom_data = request.study_id
        logger.info(f"Received patient_id: {fhir_data}")
        logger.info(f"Received study_id: {dicom_data}")
        patient_resource = construct_patient_resource()
        return create_new_patient(patient_resource)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))