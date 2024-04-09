# Class Variable:
# Defined at the class level and are shared among all instances of the class. Defined outside of any method and are usually used to store information that is common to all instances of the class

class Employee:
    companyName = "Apple" #Class Variable (Common for the whole class)
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02  
        Employee.noOfEmployees +=1
    def showDetails(self):
        print(f"The name is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Bunny")
emp1.raise_amount = 0.3 #Instance Variable (Object)
emp1.companyName = "Apple India" #Instance Variable > Class Variable (Overwrites the class Variable)
emp1.showDetails()
emp2 = Employee("Ayush")
emp2.showDetails()