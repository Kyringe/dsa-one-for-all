# Swapping elements in array
def swap(index, pos1, pos2):
    temp = index[pos1]
    index[pos1]=index[pos2]
    index[pos2]=temp
    return index
index = [23, 65, 19, 90]
pos1, pos2 = 1,3
print("Before swapping: ", index)
print("After swapping: ", swap(index, pos1, pos2))