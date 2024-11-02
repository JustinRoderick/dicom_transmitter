from fastapi import APIRouter
from ..api.dicom_handler import retrieve_dicom

router = APIRouter()

@router.get("/dicom/{accession_number}")
async def get_dicom(accession_number: str):
    return retrieve_dicom(accession_number)