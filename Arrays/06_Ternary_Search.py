def ternary_search(arr, target, left, right):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) //3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target <arr[mid1]:
            return ternary_search(arr, target, left, mid1-1)
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2+1, right)
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)
    return -1

arr = list(map(int, input("Enter the elements in array: ").split()))
arr.sort()
target = int(input("Enter the element to be searched for: "))
index = ternary_search(arr, target, 0, len(arr) - 1)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in array {arr}")