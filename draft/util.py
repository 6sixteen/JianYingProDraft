import os
import shutil
import uuid
import json
from pathlib import Path
import mimetypes  
import platform
from time import time

def get_time():
    t = time()
    return int(t)

def get_time_ms():
    t = time() * 1000000
    return int(t)
def judge_image_path(path:Path):
    mimetype = mimetypes.guess_type(str(path))[0]  
    return 'image' in mimetype.split('/')

def get_system():
    sys:str = platform.system()
    return sys.lower()
def generate_id():
    """
        生成uuid
    """
    return str(uuid.uuid4()).upper()

def write_json(path,data):
    with open(path,'w') as file:
        json.dump(data,file)

def read_json(path):
    with open(path,'r') as file:
        return json.load(file)

def new_folder(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    else:
        os.mkdir(folder_path)
