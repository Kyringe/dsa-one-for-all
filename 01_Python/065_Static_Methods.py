# These methods belong to a class rather than an instance of the class. They do not have access to the instance of the class (i.e. self)

class Math:
    def __init__(self, num):
        self.num = num
    
    def addToNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a,b): #You do not require self here
        return a+b
a = Math(5)
print(a.num)
a.addToNum(6)
print(a.num)

print(Math.add(2,5)) #Static method call