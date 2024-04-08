# Basic operations on arrays
# Accessing elements
a = [10, 20, 30, 40, 50]
print(a[0])
print(a[1])

# Inserting elements
b = [10, 20, 30, 40, 50]
b.append(100) #Inserts the element in the end
print(b)
b.insert(2,25) #At position 2, element inserted 25
print(b)

# Deleting elements
c = [10, 20, 30, 40, 50] 
c.pop(2) #Removing element at index 2
print(c)
c.remove(40) #Removing element 30
print(c)

# Traversing elements
d = [10, 20, 30, 40, 50]
index = d.index(30)
print(index)

# Manipulating elements
e = [50,10,40,30,20]
e.sort() #Sorting in ascending order
print(e)
e.reverse()
print(e)