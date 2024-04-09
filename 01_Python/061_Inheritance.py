# Inherits properties of parent class

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of employee is: {self.name} and id is {self.id}")

class Programmer(Employee):
    def showFunction(self):
        print("The default language is Python")
    
e1 = Employee("Bunny", 101)
e1.showDetails()
e2 = Programmer("Ayush", 102)
e2.showDetails()
e2.showFunction()
                 