# Map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements

def cube(x):
    return x*x*x
l = [1,2,3,4,5,6]
newl = (map(cube, l)) #This returns in map object
print(newl)
newl = list((map(cube, l))) #You have to write your desired datatype for output
print(newl)


# Filter function filters a sequence of elements based on a given predicate and returns a new sequence containing only the elements that meet the predicate.

def filter_function(a):
    return a>4
new = filter(filter_function, l)
print(new) #This returns filter object
new = list(filter(filter_function, l))
print(new) #You have to specify the datatype


# Reduce function is a higher order function that applies a function to a sequence and returns a single value

from functools import reduce #You have to import reduce function to use it
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y, numbers)
print (sum)