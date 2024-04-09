# Enumerate function allows to loop over a sequence and get the index and value of each element in the sequence at the same time.

marks = [12,56,32,98,12,45,1,4]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Lund")

# Can use start function too
a = [1,2,3,4,5]
for index, ab in enumerate(a, start=1):
    print(ab)
    if(index==3):
        print("Chut")