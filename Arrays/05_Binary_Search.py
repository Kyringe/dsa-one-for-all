def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left<=right:
        mid = (left+right)//2 #Using // rounds of the solution to the nearest integer
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+ 1
        else:
            right = mid-1
    return -1
arr = list(map(int, input("Enter the elements in array: ").split()))
target = int(input("Enter the element to be searched for: "))
index = binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Elements {target} not found in array {arr}")