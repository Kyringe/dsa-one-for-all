class Person:
    name = "Bunny"
    occupation = "Lund"
    networth = 1
    def info(self): #Self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
        print(f"{self.name} is a {self.occupation}")
a = Person()
a.name="Ayush"
a.info()