# WAP to show use of functions

def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    elif(a==b):
        print("Both numbers are equal")
    else:
        print("Second number is greater")

def isSmaller(a,b):
    pass #This is used when you want to complete the function after some time. Using this it wont throw any errors.

a = 9
b = 8
calculateGmean(a,b)
isGreater(a,b)
c = 15
d = 19
calculateGmean(c,d)
isGreater(c,d)