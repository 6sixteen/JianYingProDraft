import platform  
  
# 获取平台名称  
platform_name = platform.system()  
  
print("当前平台是：", platform_name)
print("操作系统的版本号:", platform.release()) #10
#返回操作系统的版本号。
print("操作系统的版本信息:", platform.version()) #10.0.22621
#返回操作系统的版本信息。
print("返回计算机的机器架构",platform.machine())
print("返回计算机的处理器类型",platform.processor())
