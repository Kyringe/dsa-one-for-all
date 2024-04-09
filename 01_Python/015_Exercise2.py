import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
print(hour)
if 0 < hour < 12:
    print("Good Morning sir")
elif 12 <= hour < 17:
    print("Good Afternoon sir")
elif 17 <= hour < 24:
    print("Good Evening Sir")
else:
    print("Enter valid time")