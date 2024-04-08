# Getters are used to access the values of an objects properties

class MyClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}")

    @property #Used to apply getter method
    def new_value(self):
        return 10 * self.value
     
obj = MyClass(10)
# obj.new_value = 67
obj.show()
print(obj.new_value) #To call a getter method

print('\n')

# Setter Method

class MyClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}")

    @property #Used to apply getter method
    def new_value(self):
        return 10 * self.value
    
    @new_value.setter #Setter Method
    def new_value(self, loda):
        self.value = loda/10

obj = MyClass(10)
obj.new_value = 67
obj.show()
print(obj.new_value) #To call a getter method