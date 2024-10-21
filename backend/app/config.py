import os
from dotenv import load_dotenv

load_dotenv()

ORTHANC_URL = os.getenv("ORTHANC_URL", "http://localhost:8042")