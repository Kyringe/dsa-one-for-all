def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1
arr = list(map(int, input("Enter the elements in array: ").split()))
target = int(input("Enter the element to search for: "))
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in {arr} array")