# Used to create and initialize an object of a class. Invoked automatically when an object of a class is created.

# Default Constructor

class Details:
    def __init__(self):
        print("Lawda E Lassan") 
obj1 = Details()

# Parameterized constructor
class Person:
    def __init__(self, n, o):
        print("Hello Lund") 
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a = Person("Bunny", "Bhosada")
a.info()
b = Person("Ayush", "Bhosadchodau")
b.info()