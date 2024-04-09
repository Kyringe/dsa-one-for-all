# Is compares exact location of object in memory
# == compares value

a = [1,2,43]
b = [1,2,43]
print(a is b)
print(a == b)

# Immutable or constants is always true for both.
print('\n')
x = 3
y = 3
print(x is y) 
print(x == y)

print('\n')
a = (1,2)
b = (1,2)
print(a is b)
print(a == b)