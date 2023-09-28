import requests
import os
from utils.verify_checksum import verify_checksum
from dotenv import load_dotenv
from utils.constants import FILE_NAME
import time
load_dotenv()

print("welcome")
time.sleep(30)
print("starting...")
URL = os.getenv('URL')

i = 0
while (i<20):

    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        file_content = data.get("file")
        # Save the file
        home_dir = os.path.expanduser("~")
        dir_path = os.path.join(home_dir, "/clientdata")
        with open(f"{dir_path}/{FILE_NAME}", "w") as file:
            file.write(file_content)

        print(f"File '{FILE_NAME}' received successfully.")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

    if verify_checksum(data.get("checksum")):
        print("Checksum Matched")
    else:
        print("Checksum not Matched \n")
    
    i+=1
    time.sleep(5)

print("exiting")