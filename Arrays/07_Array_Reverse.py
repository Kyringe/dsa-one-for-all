# Array reverse using an extra array
def array_reverse(arr):
    reversed_arr = arr[::-1]
    print("Reversed array: ", end = " ")
    for i in reversed_arr:
        print (i, end=" ")
arr = list(map(int, input("Enter the elements of array: ").split()))
print("Original array: ", arr)
array_reverse(arr)

print('\n')

# Array reverse using loop
def array_reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
arr = list(map(int, input("Enter the elements of array: ").split()))
print("Original array: ", arr)
array_reverse(arr, 0, len(arr)-1)
print("Reversed list: ", arr)

print('\n')

# Array reverse using recursion 
def array_reverse(arr, start, end):
    if start >= end:
        return 
    arr[start], arr[end] = arr[end], arr[start]
    array_reverse(arr, start+1, end-1)
arr = list(map(int, input("Enter the elements of array: ").split()))
print("Original array: ", arr)
array_reverse(arr, 0, len(arr)-1)
print("Reversed array: ", arr)

print('\n')

# Array reverse using stack
def array_reverse(arr):
    stack = []
    for i in arr:
        stack.append(i)
    for i in range(len(arr)):
        arr[i] = stack.pop()
arr = list(map(int, input("Enter the elements of array: ").split()))
print("Original array: ", arr)
array_reverse(arr)
print("Reversed array: ", arr)