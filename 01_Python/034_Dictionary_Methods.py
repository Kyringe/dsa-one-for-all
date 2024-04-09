eid1 = {
    101: 45, 102: 89, 103: 69, 104: 69
}
eid2 = {
    201: 67, 202: 90
}

#Update method
eid1.update(eid2)
print(eid1)

#Pops a key with its value from the dictionary
eid1.pop(101)
print(eid1)

#Pop item removes the last key-value pair from the dictionary
eid1.popitem()
print(eid1)

#Empty dictionary
empty = {}
print(empty)
 
#Del keyword deletes the dictionary completely
del eid1[103] #If the key value is not present in the dictionary then it deletes the entire dictionary
print(eid1) 

#Clear method. Removes all the elements from the dictionary
eid1.clear()
print(eid1)

