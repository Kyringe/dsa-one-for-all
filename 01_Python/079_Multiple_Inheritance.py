class Class1:
    def m(self):
        print("Class 1")
class Class2(Class1):
    def m(self):
        print("Class 2")
class Class3(Class1):
    def m(self):
        print("Class3")
class Class4(Class2, Class3): #The method written first in the bracket is returned no matter what
    pass
obj = Class4()
obj.m()