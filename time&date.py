from datetime import timezone, time, date, datetime

d1 = date(2025,7,1)
d2 = date(2025,7,23)

diff = d2 - d1

print(diff.days)

t_string = "02:30 pm"
t_obj = datetime.strptime(t_string, "%I:%M %p").time()
print(t_obj)  # Output: 14:30:00


import time

time.sleep(2) # Delay 2 second