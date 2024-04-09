# Array rotation on left

def left_rotation(arr, d):
    n = len(arr)
    d = d % n
    rotated_arr = arr[d:] + arr[:d]
    return rotated_arr
arr = list(map(int, input("Enter the elements of array: ").split()))
d = int(input("Enter the number of positions to rotate left: "))
rotated_arr = left_rotation(arr, d)
print("Original array: ", arr)
print(f"Rotated array after {d} rotations: ", rotated_arr)

print('\n')

# Array rotation on right

def right_rotation(arr, d):
    n = len(arr)
    d = d % n
    rotated_arr =  arr[-d:] + arr[:-d]
    return rotated_arr
arr = list(map(int, input("Enter the elements of array: ").split()))
d = int(input("Enter the number of positions to rotate right: "))
rotated_arr = right_rotation(arr, d)
print("Original array: ", arr)
print(f"Rotated array after {d} rotations: ", rotated_arr)