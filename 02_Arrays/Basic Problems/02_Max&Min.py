# Max & Min of a function using sorting

def getMinMax(arr):
    arr.sort()
    minmax = {"min": arr[0], "max": arr[-1]}
    return minmax
arr = list(map(int, input("Enter elements of array: ").split()))
minmax = getMinMax(arr)
print("Minimum element is", minmax["min"])
print("Maximum element is", minmax["max"])
