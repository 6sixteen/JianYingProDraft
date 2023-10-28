import os
import shutil
import uuid
import json
from pathlib import Path
import mimetypes  
import platform
from time import time
from pydub import AudioSegment  
from typing import Union

def get_mp3_duration(file_path: Union[str, Path], base: int = 1000000) -> int:
    """
    Calculate the duration of an MP3 file.

    Args:
        file_path (Union[str, Path]): The path to the MP3 file.
        base (int): The base to multiply the duration by. Default is 1000000.

    Returns:
        int: The duration of the MP3 file multiplied by the base.
    """
    # Convert file_path to string if it's a Path object
    file_path = str(file_path)

    # Load the audio segment from the file
    audio = AudioSegment.from_file(file_path, format="mp3")

    # Get the duration in seconds
    duration = audio.duration_seconds

    # Return the duration multiplied by the base
    return int(duration * base)

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
