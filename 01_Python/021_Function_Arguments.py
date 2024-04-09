# WAP to show function arguments

# Default Arguments
def name(fname, mname="Bunny", lname="Ayush"):
    print("Hello", fname, mname, lname)
name("Ankur")

# Keyword Arguments; Order in which arguments are passed does not matter
def name(fname, mname, lname):
    print("Hello", fname, mname, lname)
name(mname="Sharan", lname="Gaur", fname="Ayush")


# Required Arguments; You have to give value in positional order if its value is not defined in the function

# Arbitrary Arguments
def average(*numbers): #Takes numbers as tuple
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/len(numbers))
average(5,6,7)

# Keyword Arbitrary Arguments

def name(**name): #Takes names as dictionary
    print(type(name))
    print("Hello, ", name["fname"],name["mname"],name["lname"])
name(mname="Sharan",lname="Gaur",fname="Ayush")
