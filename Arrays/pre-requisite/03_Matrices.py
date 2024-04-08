row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
matrix = []
print("Enter the entries row wise: ")
for i in range(row): #For user input
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)

for i in range(row):
    for j in range(column):
        print(matrix[i] [j], end = ' ')
    print()