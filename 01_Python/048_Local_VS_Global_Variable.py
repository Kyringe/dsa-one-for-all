# WAP to show local and global variable usage

x = 4
def hello():
    x = 5
    print(f"The local is {x}")
print(f"The global is {x}")
hello()

# To change global varibale in local variable

a = 10
def new():
    global a
    a = 1
    b = 9 #Local Variable
    print(b)
new()
print(a)