import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.fhir_handler import *
from api.dicom_handler import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

class PatientRequest(BaseModel):
    patient_id: str
    study_id: str

@router.post("/process-patient-data")
async def process_patient_data(request: PatientRequest):
    try:
        patient_mrn = request.patient_id
        patient_accession_num = request.study_id
        logger.info(f"Received mrn: {patient_mrn}")
        logger.info(f"Received accession_num: {patient_accession_num}")
        
        orthanc_study_result = query_orthanc_id_by_accession(patient_accession_num)
        if "error" in orthanc_study_result:
            raise HTTPException(status_code=404, detail="Study not found in Orthanc")
        logger.info(f"Matched Orthanc study ID: {orthanc_study_result}")

        patient_result = query_patient_id_by_mrn(patient_mrn)
        if "error" in patient_result:
            raise HTTPException(status_code=404, detail="Patient not found in Orthanc")
        logger.info(f"Matched Orthanc patient ID: {patient_result}")

        patient_resource = construct_patient_resource()
        create_new_patient_result = create_new_patient(patient_resource)

        return {
            "message": "Patient data processed successfully",
            "fhir_result": create_new_patient_result,
            "orthanc": {
                "study_id": orthanc_study_result,
                "patient_id": patient_result,
            },
        }
    except Exception as e:
        logger.error(f"Error processing patient data: {e}")
        raise HTTPException(status_code=500, detail=str(e))