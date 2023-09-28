import random
import string
import os
from utils.constants import DIR,FILE_NAME, FILE_SIZE_BYTES

def random_file_generator():
    #if not os.path.exists(DIR):
    #        os.makedirs(DIR)
            
    random_data = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(FILE_SIZE_BYTES))
    home_dir = os.path.expanduser("~")
    dir_path = os.path.join(home_dir, DIR)
    file_name = f"{dir_path}/{FILE_NAME}"


    with open(file_name, 'w') as file:
        file.write(random_data)

    print(f"Random data written to {file_name}")
    return random_data