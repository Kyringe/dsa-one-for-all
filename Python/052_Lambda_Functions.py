# Lambda function is a small anonymous function without a name.
# They are often used in situations where a small function is required for a short period of time

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y: (x+y)/2
print(double(5))
print(cube(2))
print(avg(4,8))

# You can do it the traditional way of declaring a function and then printing it.
# It is just a shorthand

# Used mainly to pass function as an argument

def appl(fx,value):
    return 6+fx(value)
print(appl(cube,2))