# Dir method

x = [1,2,3]
print(dir(x))

print('\n')

# Dict method gives details of all the attributes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p = Person("Bunny",30)
print(p.__dict__)

print('\n')
print(help(Person)) # Help Method: Gives documentation of the parameter you need