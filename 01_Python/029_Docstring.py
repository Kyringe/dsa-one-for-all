# WAP to show use of docstring

def square(n):
    ''' Takes in a number n, returns the square of n''' #It has to be just below where you define the function.
    print(n*n)
square (5)
print(square.__doc__)