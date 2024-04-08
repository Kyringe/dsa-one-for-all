class Parent:
    def func1(self):
        print("This function is in parent class")
class Child(Parent):
    def func2(self):
        print("This function is in child class")
obj = Child()
obj.func1()
obj.func2()