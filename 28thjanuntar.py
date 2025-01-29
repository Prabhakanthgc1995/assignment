import tarfile
import os

# Specify the path to the tar.gz file
tar_file_path = "/home/ubuntu/behave.tar.gz"

# Specify the directory where the files will be extracted
extract_to_path = "/home/ubuntu/"

# Ensure the extraction directory exists
os.makedirs(extract_to_path, exist_ok=True)

# Open and extract the tar.gz file
with tarfile.open(tar_file_path, 'r:gz') as tar_ref:
    tar_ref.extractall(extract_to_path)

print(f"Files extracted to: {extract_to_path}")

