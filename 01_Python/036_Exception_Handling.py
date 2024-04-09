#WAP to show exception handline

a = input("Enter a number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1.11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except Exception as e:
    print(e)
    print("Invalid input")
print("Some imp lines of code") #The rest of the code is executed even if there is error in input
print("End of program")

