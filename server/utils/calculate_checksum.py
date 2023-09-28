import hashlib
from utils.constants import DIR, FILE_NAME



def calculate_checksum():
    md5_hash = hashlib.md5()
    with open(f"{DIR}/{FILE_NAME}", "rb") as file:
        # Read the file in chunks to handle large files
        while chunk := file.read(8192):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

