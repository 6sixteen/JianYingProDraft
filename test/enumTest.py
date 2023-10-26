import json
from enum import Enum
from pathlib import Path 

root = Path(__file__).resolve().parent
temp_path = root / "temp"

def test_json_enum():
    class Person(Enum):
        plh = "plh"
        lbw = "lbw"
    class EnumEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, Enum):
                    return obj.value
                return super().default(obj)
    data = {"a":Person.plh}
    # 将字典转换为 JSON 格式  
    json_data = json.dumps(data,cls=EnumEncoder,indent=2) 
    json_path = temp_path / "enumjson.json"
    with open(json_path, "w") as f:  
            f.write(json_data)

if __name__ == "__main__":
    test_json_enum()