import time
timestamp = time.strftime('%H:%M:%S:%p:%u')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
timestamp = time.strftime('%p')
print(timestamp)
timestamp = time.strftime('%u')
print(timestamp)

import time

Day = int(time.strftime('%u'))  # 1=Mon, 7=Sun
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Today is a",days[Day - 1])



import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))
minute = int(time.strftime('%S'))
second = int(time.strftime('%S'))


print(hour)
print(minute)
print(second)

#Greeting based on hour

if hour>= 0 and hour < 12:
    print("Good Morning Sir!")
elif hour >= 12 and hour < 16:
    print("Good Afternoon Sir!")
elif hour >= 16 and hour < 20:
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")


# https://docs.python.org/3/library/time.html#time.strftime