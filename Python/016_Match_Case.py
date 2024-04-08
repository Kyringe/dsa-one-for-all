#WAP to use match case

x = int(input("Enter a number between 1-4: "))
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case _:
        print("Enter valid number")