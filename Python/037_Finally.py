# Prints the block of code in finally whether error occurs or not

try:
    l = [1,3,5,7,9]
    i = int(input("Enter index "))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("Always executes")