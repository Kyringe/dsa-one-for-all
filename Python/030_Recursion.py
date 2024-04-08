# WAP to show use of recursion

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* factorial (n-1)
print(factorial(5))


# WAP to print fibonacci series

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def print_fibonacci_series(count):
    if count <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:")
        for i in range(count):
            print(fibonacci(i), end=" ")
count = 10  
print_fibonacci_series(count)