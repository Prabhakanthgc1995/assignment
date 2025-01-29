import json
import requests
import tarfile

# Load the JSON data
with open("/root/1.json", "r") as fh:
    json_data = json.load(fh)

# Define the tar file path
file_path = "/home/ubuntu/behave.tar.gz"

# Loop through the JSON data and download the tar file
for ele in json_data:
    source_url = ele["Source URL"]
    response = requests.get(source_url)

    # Save the tar file to the specified file path
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    print("Tar file downloaded successfully.")
    break  # If you only want to download the first URL in the JSON data

print("outside the for loop")

# Open the tar file for extraction
with tarfile.open(file_path) as file:
    # Extract all contents to a specific directory
    file.extractall('/home/ubuntu/behave_extract/')  # Change this path if needed

print("Extraction completed.")

