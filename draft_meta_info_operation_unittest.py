
from pathlib import Path
from draftcontent import *
from dataclasses import asdict
import json
from draft_meta_info_operation import DraftMetaInfoOperation
from draft_meta_info import *

root = Path(__file__).resolve().parent
temp_path = root / "temp"
print(temp_path)

def test_write_json():
    draft_meta_info = DraftMetaInfo(draft_fold_path="D:/JianyingPro Drafts/10月25日",
        draft_name="empty_project",
        draft_removable_storage_device="D:",
        draft_root_path="D:\\JianyingPro Drafts",
        )
    # 将字典转换为 JSON 格式  
    json_path = temp_path / "my_empty_draft_meta_info.json"
    DraftMetaInfoOperation.write2json(draft_meta_info, json_path)

def test_add_img():
    draft_meta_info = DraftMetaInfo(draft_fold_path="D:/JianyingPro Drafts/one image",
        draft_name="one_image",
        draft_removable_storage_device="D:",
        draft_root_path="D:\\JianyingPro Drafts",)
    img_path= Path("D:/PersonalProjects/Moody Blues Project old/Moody Blues/temp/imgs/test-generate-prompt/output_001.jpg")
    draft_meta_info = DraftMetaInfoOperation.add_image(draft_meta_info,img_path=img_path)
    json_path = temp_path / "my_first_image_draft_meta_info.json"
    DraftMetaInfoOperation.write2json(draft_meta_info, json_path)

def test_add_2img():
    draft_meta_info = DraftMetaInfo(draft_fold_path="D:/JianyingPro Drafts/two_image",
        draft_name="two_image",
        draft_removable_storage_device="D:",
        draft_root_path="D:\\JianyingPro Drafts",)
    img_path= Path("D:/PersonalProjects/Moody Blues Project old/Moody Blues/temp/imgs/test-generate-prompt/output_001.jpg")
    draft_meta_info = DraftMetaInfoOperation.add_image(draft_meta_info,img_path=img_path)
    img_path= Path("D:/PersonalProjects/Moody Blues Project old/Moody Blues/temp/imgs/test-generate-prompt/output_002.jpg")
    draft_meta_info = DraftMetaInfoOperation.add_image(draft_meta_info,img_path=img_path)
    json_path = temp_path / "my_two_image_draft_meta_info.json"
    DraftMetaInfoOperation.write2json(draft_meta_info, json_path)

def make_dir(dir_path):
    draft_root_path="D:\\JianyingPro Drafts"
    draft_fold_path="D:/JianyingPro Drafts/10月25日"

if __name__ == "__main__":
    # test_write_json()
    # test_add_img()
    test_add_2img()