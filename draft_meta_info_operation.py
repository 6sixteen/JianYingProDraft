from draft_meta_info import *
from pathlib import Path 
import json 
from enum import Enum 
from dataclasses import asdict
from PIL import Image
from draft.util import judge_image_path,get_mp3_duration

class DraftMetaInfoOperation:

    @classmethod
    def __add_draft_materials_type7_type8(self,meta_info:DraftMetaInfo):
        draft_materials:list =  meta_info.draft_materials
        type7_flag = False
        type8_flag = False
        for draft_material in draft_materials:
            if draft_material.type == 7:
                type7_flag = True
            if draft_material.type == 8:
                type8_flag = True
        if not type7_flag:
            draft_material_type7 = DraftMaterial(7)
            draft_materials.append(draft_material_type7)
        if not type8_flag:
            draft_material_type8 = DraftMaterial(8)
            draft_materials.append(draft_material_type8)
    @classmethod
    def write2json(self,draft_content:DraftMetaInfo,json_path:Path,ensure_ascii=False,encoding='utf-8'):
        class EnumEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, Enum):
                    return obj.value
                if isinstance(obj,Path):
                    return str(obj)
                return super().default(obj)
        data = asdict(draft_content)
    # 将字典转换为 JSON 格式  
        json_data = json.dumps(data,cls=EnumEncoder,indent=2,ensure_ascii=ensure_ascii) 
        # 将 JSON 数据写入文件  
        with open(json_path, "w", encoding=encoding) as f:  
            f.write(json_data)

    @classmethod
    def add_image(cls,draft_meta_info:DraftMetaInfo,img_path:Path):
        if not judge_image_path(img_path):
            raise FileNotFoundError("This path is not an image file")
        if not img_path.exists():
            raise FileNotFoundError("no image")
        img = Image.open(img_path) 
        w, h = img.size  
        img_name = img_path.name
        draft_materials:list =  draft_meta_info.draft_materials
        draft_material_type0:DraftMaterial =  draft_materials[0]
        draft_material_type0_value_list:list = draft_material_type0.value
        
        if len(draft_material_type0_value_list) == 0:
            #init
            draft_material_type7 = DraftMaterial(7)
            draft_material_type8 = DraftMaterial(8)
            draft_materials.extend([draft_material_type7,draft_material_type8])

        draft_material_type0_value = DraftMaterialType0(
            file_path=str(img_path),
            extra_info=img_name,
            height=h,
            width=w)
        draft_material_type0_value_list.append(draft_material_type0_value)
        

        return draft_meta_info
    
    @classmethod
    def add_audio(cls,draft_meta_info:DraftMetaInfo,audio_path:Path):
        if not audio_path.exists():
            raise FileNotFoundError("no audio")
        cls.__add_draft_materials_type7_type8(draft_meta_info)

        audio_name = audio_path.name
        audio_duration = get_mp3_duration(audio_path)
        draft_materials:list =  draft_meta_info.draft_materials
        draft_material_type0:DraftMaterial =  draft_materials[0]
        draft_material_type0_value_list:list = draft_material_type0.value

        draft_material_type0_value = DraftMaterialType0(
            file_path=str(audio_path),
            extra_info=audio_name,
            duration=audio_duration,
            metetype="music")
        draft_material_type0_value.roughcut_time_range.duration = audio_duration
        draft_material_type0_value.roughcut_time_range.start = 0
        draft_material_type0_value_list.append(draft_material_type0_value)
        
        return draft_meta_info,draft_material_type0_value.id
    