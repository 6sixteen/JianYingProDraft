class MyClass:
    def __init__(self, value):
        self.value = value

    @classmethod
    def class_method(cls, x):
        print(f"This is a class method. Value: {x}")
        cls.normal_method(x)  # 在类方法中调用普通方法，并传递参数

    def normal_method(self, y):
        print(f"This is a normal method. Value: {y}")

# 使用类方法
MyClass.class_method(10)

