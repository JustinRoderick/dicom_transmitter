from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import fhir, dicom, patient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # Change to prod frontend URL later
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fhir.router)
app.include_router(dicom.router)
app.include_router(patient.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/testroute")
async def read_test():
    return {"test": "test route exists"}