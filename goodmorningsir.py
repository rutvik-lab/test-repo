import time

# Full timestamp
timestamp = time.strftime('%H:%M:%S:%p:%u')
print("Full Timestamp:", timestamp)

# Individual parts
print("Hour:", time.strftime('%H'))
print("Minute:", time.strftime('%M'))
print("Second:", time.strftime('%S'))
print("AM/PM:", time.strftime('%p'))
print("Day Number (1=Mon, 7=Sun):", time.strftime('%u'))

# Day of the week
Day = int(time.strftime('%u'))  # 1=Mon, 7=Sun
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Today is", days[Day - 1])

# Current time
timestamp = time.strftime('%H:%M:%S')
print("Current Time:", timestamp)

# Extract parts as integers
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)

# Greeting based on hour
if 0 <= hour < 12:
    print("Good Morning Sir!")
elif 12 <= hour < 16:
    print("Good Afternoon Sir!")
elif 16 <= hour < 20:
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")
