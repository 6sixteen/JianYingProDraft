import unittest
from unittest.mock import MagicMock
from PIL import Image
from pathlib import Path
from draftcontent import *
from dataclasses import asdict
import json
from draftoperation import DraftOperation

root = Path(__file__).resolve().parent
temp_path = root / "temp"
print(temp_path)

def test_dict():
    draft_content = DraftContent()
    # 将字典转换为 JSON 格式  
    json_path = temp_path / "my_empty_draft_content.json"
    DraftOperation.write2json(draft_content, json_path)

def test_add_first_image2track():
    draft_content = DraftContent()
    image_path = Path("D:/PersonalProjects/Moody Blues Project old/Moody Blues/temp/imgs/test-generate-prompt/output_001.jpg")
    draft_content = DraftOperation.add_image2track(draft_content, image_path)
    json_path = temp_path / "first_image2track.json"
    DraftOperation.write2json(draft_content, json_path)
if __name__ == "__main__":
    # test_dict()
    test_add_first_image2track()

