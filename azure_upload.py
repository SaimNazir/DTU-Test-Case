from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
from azure.core.exceptions import ResourceExistsError
from dotenv import load_dotenv
import os

load_dotenv('.env')

# Azure Storage account details
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = "container"
local_file_path = "/home/saim/dtu_test_case/test.txt"
blob_name = "test_blob.txt"


blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

try:
    container_client.create_container()
    print(f"Container '{container_name}' created successfully.")
except ResourceExistsError:
    print(f"Container '{container_name}' already exists.")

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"File '{local_file_path}' uploaded to Azure Blob Storage as '{blob_name}' in container '{container_name}'.")
