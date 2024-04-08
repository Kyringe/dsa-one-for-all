# WAP to show list methods

l = [11,33,5,7,5]
print(l)

print(l.append(9)) #Adds 9 to the end of the list
print(l)

l.sort() #Sorts the list
print(l)

l.sort(reverse=True)
print(l)

print(l.index(5))
print(l.count(5)) #Counts how many times 5 occured

l.insert(1,299)
print(l)

# Concatenating two lists
a = [10,20,30]
b = [100, 200, 300]
c = b+a
print(c)