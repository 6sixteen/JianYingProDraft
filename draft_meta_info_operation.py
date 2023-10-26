from draft_meta_info import *
from pathlib import Path 
import json 
from enum import Enum 
from dataclasses import asdict

class DraftMetaInfoOperation:


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