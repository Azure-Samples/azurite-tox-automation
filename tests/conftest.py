from types import TracebackType
from azure.storage.blob import BlobServiceClient,ContainerClient
import os
from dotenv import load_dotenv
import pdb

def pytest_generate_tests(metafunc):
    # We are going to reproduce the same scenario in app.py but this time in storage emulator Azurite
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".test_env"))

    # Azurite connection
    blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("AZURITE_CONNECTION_STRING"))
    
    try:
        #create a dummy container
        container = blob_service_client.create_container(os.environ.get("AZURITE_STORAGE_CONTAINER"))
        #upload data into blob
        with open("./data/data.txt", "rb") as data:
            blob_service_client.upload_blob(data,overwrite=True)
    except Exception as e:
        print(e)
        return False