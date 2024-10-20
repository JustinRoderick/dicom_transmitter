from fastapi import FastAPI
from .routers import fhir, dicom

app = FastAPI()

app.include_router(fhir.router)
app.include_router(dicom.router)