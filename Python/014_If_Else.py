# WAP to check whether a person can drive or not using if else conditional statement

a = int(input("Enter your age: "))
print("Your age is: ",a)
if(a>18):
    print("You can drive")
elif(a==18):
    print("You can apply for learners lisence ")
else:
    print("You cannot drive")