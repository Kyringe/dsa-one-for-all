def subarray(arr, start, end, result):
    if start > end:
        return
    temp = []
    for i in range(start, end + 1):
        temp.append(arr[i])
        result.append(temp.copy())
    subarray(arr, start + 1, end, result)

arr = list(map(int, input("Enter the elements of array: ").split()))
result = []
subarray(arr, 0, len(arr) - 1, result)
print("All subarrays:")
for subarray in result:
    print(subarray)
