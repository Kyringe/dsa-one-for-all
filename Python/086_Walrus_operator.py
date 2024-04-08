# Walrus operator allows you to assign a value to a variable within an expression.

print(a:=False)

numbers = [1,2,3,4,5]
while (n := len(numbers)) > 0:
    print(numbers.pop())