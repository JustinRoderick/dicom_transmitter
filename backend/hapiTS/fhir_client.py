import os
import requests
from fhirpy import SyncFHIRClient
from dotenv import load_dotenv
import base64

# Load environment variables from the .env file
load_dotenv()

# Define FHIR server configuration
FHIR_SERVER_URL = os.getenv("FHIR_SERVER_URL", "http://localhost:8080/fhir")
FHIR_USERNAME = os.getenv("FHIR_USERNAME", "your-username")
FHIR_PASSWORD = os.getenv("FHIR_PASSWORD", "your-password")

# DICOM server base URL
DICOM_SERVER_URL = os.getenv("DICOM_SERVER_URL", "http://localhost:8000")

# Encode the username and password in base64 for Basic Authentication
auth_token = base64.b64encode(f"{FHIR_USERNAME}:{FHIR_PASSWORD}".encode()).decode()

# Initialize FHIR client with custom headers for Basic Authentication
client = SyncFHIRClient(
    FHIR_SERVER_URL,
    extra_headers={"Authorization": f"Basic {auth_token}"}
)

# CREATE: Function to create a new Patient
def create_patient(mrn, patient_id, family_name, given_name, gender="unknown", birth_date="1900-01-01"):
    """
    Create a new Patient in the FHIR server.
    """
    new_patient = client.resource(
        "Patient",
        identifier=[
            {"system": "http://hospital.org/mrn", "value": mrn},
            {"system": "http://hospital.org/patient-id", "value": patient_id}
        ],
        name=[{"use": "official", "family": family_name, "given": [given_name]}],
        gender=gender,
        birthDate=birth_date
    )
    new_patient.save()
    print("Created Patient:", new_patient)
    return new_patient

# READ: Function to retrieve a Patient by MRN
def get_patient_by_mrn(mrn):
    """
    Retrieve a Patient from the FHIR server by MRN.
    """
    patient = client.resources("Patient").search(identifier=mrn).first()
    if patient:
        print("Retrieved Patient:")
        print("MRN:", mrn)
        print("ID:", patient.id)
        print("Name:", " ".join(patient["name"][0]["given"]) + " " + patient["name"][0]["family"])
        print("Gender:", patient.get("gender", "N/A"))
        print("Birth Date:", patient.get("birthDate", "N/A"))
    else:
        print("No Patient found with MRN:", mrn)
    return patient

# FETCH: Function to retrieve Patient details from DICOM server
def get_patient_from_dicom(study_id):
    """
    Fetch Patient details (name, birthdate) from the DICOM server.
    """
    try:
        response = requests.get(f"{DICOM_SERVER_URL}/dicom/{study_id}/Patient")
        response.raise_for_status()
        data = response.json()
        print("Retrieved Patient from DICOM:", data)
        return data
    except requests.RequestException as e:
        print("Error fetching Patient from DICOM server:", e)
        return None

# CREATE FROM DICOM: Function to create a new Patient using DICOM data
def create_patient_from_dicom(study_id, mrn, patient_id):
    """
    Create a new Patient in the FHIR server using data from the DICOM server.
    """
    dicom_patient = get_patient_from_dicom(study_id)
    if not dicom_patient:
        print("Failed to create Patient from DICOM data.")
        return None

    return create_patient(
        mrn=mrn,
        patient_id=patient_id,
        family_name=dicom_patient["name"].split(" ")[-1],  # Assuming "John Doe" format
        given_name=" ".join(dicom_patient["name"].split(" ")[:-1]),  # Extract first names
        gender=dicom_patient.get("gender", "unknown"),
        birth_date=dicom_patient.get("birthdate", "1900-01-01")
    )

# DELETE: Function to delete a Patient
def delete_patient(patient):
    """
    Delete a specific Patient from the FHIR server.
    """
    patient.delete()
    print("Deleted Patient with ID:", patient.id)

# CLEAR ALL: Function to delete all Patients
def clear_all_patients():
    """
    Clear all Patients from the FHIR server.
    """
    patients = client.resources("Patient").fetch_all()
    for patient in patients:
        patient.delete()
        print("Deleted Patient with ID:", patient.id)
    print("All Patients have been deleted.")

# DICOM Functions for Studies and Series
def get_studies_by_mrn(mrn):
    """
    Retrieve Studies for a Patient by MRN from Orthanc.
    """
    url = f"{DICOM_SERVER_URL}/Patients"
    response = requests.get(url)
    if response.status_code == 200:
        patients = response.json()
        for patient_id in patients:
            patient_details = requests.get(f"{DICOM_SERVER_URL}/Patients/{patient_id}").json()
            if patient_details["MainDicomTags"]["PatientID"] == mrn:
                studies = patient_details.get("Studies", [])
                return studies
    return None


def get_series_by_study(study_id):
    """
    Retrieve Series for a specific Study from Orthanc.
    """
    url = f"{DICOM_SERVER_URL}/Studies/{study_id}/Series"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Example operations
if __name__ == "__main__":
    # Example: Create a Patient using DICOM data
    study_id = "STUDY12345"
    created_patient = create_patient_from_dicom(
        study_id=study_id,
        mrn="MRN12345",
        patient_id="PID67890"
    )

    # Retrieve the Patient by MRN
    if created_patient:
        get_patient_by_mrn("MRN12345")

    # Uncomment to clear all Patients
    # clear_all_patients()