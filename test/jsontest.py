import json  
  
# 创建一个字典，其中包含一个 None 值  
data = {  
    "name": "John",  
    "age": None,  
    "address": {  
        "street": "123 Main St",  
        "city": None,  
        "state": "CA"  
    }  
}  
  
# 将字典转换为 JSON 格式  
json_data = json.dumps(data,indent=2)  
  
# 将 JSON 数据写入文件  
with open("data.json", "w") as f:  
    f.write(json_data)