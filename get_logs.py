import zipfile
import subprocess

# Azure subscription and resource details
resource_group_name = "Zoomcamp"
app_name = "my-app"

# Download the logs using Azure CLI
command = f"az webapp log download --resource-group {resource_group_name} --name {app_name} --log-file azure_webapp_logs.zip"

subprocess.run(command, shell=True, check=True)

with zipfile.ZipFile('azure_webapp_logs.zip', 'r') as zip_ref:
    zip_ref.extractall('logs')

print("Logs have been downloaded and extracted.")
