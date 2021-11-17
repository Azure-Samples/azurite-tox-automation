from typing import List
from azure.storage.blob.aio import BlobClient, BlobServiceClient
from fastapi import APIRouter
import os 
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

router = APIRouter(
    prefix = "/api",
    tags=["data"]
)

@router.get("/create")
async def upload_blob():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("STORAGE_CONNECTION_STRING"))
        container = blob_service_client.get_container_client(os.environ.get("STORAGE_CONTAINER"))
        
        if container.account_name == "" or None :
            await blob_service_client.create_container(os.environ.get("STORAGE_CONTAINER"))
            
        with open("../data/data.txt", "rb") as data:
            blob_client = container.get_blob_client("data.txt")
            await blob_client.upload_blob(data,overwrite=True)
    except Exception as e:
        print(e)
        return False

@router.get("/download", response_model=List[str])
async def download_blob():
    try:
        blob = BlobClient.from_connection_string(conn_str=os.environ.get("STORAGE_CONNECTION_STRING"),\
                container_name=os.environ.get("STORAGE_CONTAINER"),
                blob_name="data")
        file_download_path = "./data/download.txt"
        
        with open(file_download_path, "wb") as file_download:
            blob_data = blob.download_blob()
            await blob_data.readinto(file_download)
    except Exception as e:
        print(e)
        return False