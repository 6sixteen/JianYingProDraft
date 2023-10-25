from copy import deepcopy
def test():
    class Person:
        def __init__(self,name):
            self.name = name

        def newInstance(self):
            self = Person("plh")


    p = Person("lbw")
    p.newInstance()
    print(p.name) #lbw

def test2():
    class Person:
        def __init__(self,name):
            self.name = name

        def newInstance(self):
            copy = deepcopy(self)
            print(copy.name) #lbw
            copy.name = "plh"

    p = Person("lbw")
    p.newInstance()
    print(p.name) #lbw

if __name__ == "__main__":
    test2()