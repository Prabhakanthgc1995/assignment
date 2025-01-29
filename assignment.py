import zipfile
import os

# Specify the path to the zip file
zip_file_path = "/home/ubuntu/apache-tomcat-11.0.2.zip"

# Specify the directory where the files will be extracted
extract_to_path = "/home/ubuntu/"

# Ensure the extraction directory exists
os.makedirs(extract_to_path, exist_ok=True)

try:
    # Open and extract the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)
    print(f"Files extracted to: {extract_to_path}")

except FileNotFoundError:
    print(f"Error: The file {zip_file_path} was not found.")

except zipfile.BadZipFile:
    print(f"Error: The file {zip_file_path} is not a valid zip file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

