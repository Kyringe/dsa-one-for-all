class Parent:
    def func1(self):
        print("This function is in parent class")
class Child1(Parent):
    def func2(self):
        print("This function is in Child1")
class Child2(Parent):
    def func3(self):
        print("This function is in child2")
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()