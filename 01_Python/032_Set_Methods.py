# WAP to show use of set methods

s1 = {1,2,3,4,5}
s2 = {5,7,8,9}
print(s1.union(s2))

s1.update(s2) #Update function
print(s1, s2)

print(s1.intersection(s2))

s3 = s1.symmetric_difference(s2) #This is (AUB)-(A∩B)
print(s3)

s4 = s1.difference(s2)
print(s4)

s5 = s1.isdisjoint(s2) #If both the sets have nothing in common
print(s5)

s6 = s1.issuperset(s2) #If all the elements of s1 are present in s2
print(s6)

s7 = s2.issubset(s1) #If all the elements of s2 are in s1
print(s7)

s1.add(100) #Add method
print(s1)

s1.remove(100) #Can use remove or discard either methods
# Main difference between remove and discard is that remove raises error if the element is already not present in set/list. But discard does not raise any error
print(s1)

item = s1.pop()
print(s1, item) #Pops a random value from the set as the set is unordered

s1.clear() #This method deletes all the elements present in the set 
print (s1)

del (s1) #Del is not a method it is a keyword. It deletes the entire set