# Time.time() function returns the current time as a floting point number, representing the number of seconds since the epoch(The point in time where the time module was initialized)

import time
def usingWhile():
    i = 0
    while i<5000000:
        i = i+1
        print(i)
def usingFor():
    for i in range (5000000):
        print(i)
init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)


# Time.sleep() suspends the execution of the current thread for a specified number of seconds

print(4)
time.sleep(3)
print("This is printed after three seconds")