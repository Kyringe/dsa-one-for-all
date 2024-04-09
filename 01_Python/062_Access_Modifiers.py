# Public can be accessed from anywhere
# Private members can be accessed within the class only
# Protected members are only accessible to other class members when they are inherited from it

# Public access modifier

class Employee:
    def __init__(self):
        self.name="Bunny" #By default public
a = Employee()
print(a.name)


# Private access modifier

class Lund:
    def __init__(self):
        self.__name="Ayush" #Double underscore for private
a = Lund()
# print(a.__name) Cannot be accessed directly
print(a._Lund__name) #Achieved by name mangling


# Protected access modifier

class Student:
    def __init__(self):
        self._name="Bunny" #Convention for protected
    def _funName(self): #Protected Method
        return "Bhosada"
class Subject(Student): #Can only be used when inherited from other class
    pass
obj = Student()
obj1 = Subject()
print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())
