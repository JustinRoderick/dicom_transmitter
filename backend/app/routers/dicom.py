from fastapi import APIRouter
from api import dicom_handler

router = APIRouter()

@router.get("/dicom/{accession_number}")
async def get_dicom(accession_number: str):
    return retrieve_dicom(accession_number)
