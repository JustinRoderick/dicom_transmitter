from fastapi import FastAPI
from routers import fhir, dicom

app = FastAPI()

app.include_router(fhir.router)
app.include_router(dicom.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/testroute")
async def read_test():
    return {"test": "test route exists"}
