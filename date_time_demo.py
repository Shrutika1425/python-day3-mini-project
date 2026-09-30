import datetime

now = datetime.datetime.now()
print(now)  # 2026-05-13 15:30:22.123456

print(now.year)
print(now.month)
print(now.day)



import datetime

today = datetime.date.today()
print(today)  # 2026-05-13

current_time = datetime.datetime.now().time()
print(current_time)


import datetime

my_date = datetime.date(2025, 8, 15)
print(my_date)

# Vaitag date + time
dt = datetime.datetime(2026, 1, 26, 10, 30, 0)
print(dt)




import datetime
now = datetime.datetime.now()

print(now.strftime("%d-%m-%Y"))       # 13-05-2026
print(now.strftime("%d %B %Y"))       # 13 May 2026
print(now.strftime("%A, %I:%M %p"))   # Tuesday, 03:30 PM




import datetime

d1 = datetime.date(2026, 5, 13)
d2 = datetime.date(2026, 12, 31)

diff = d2 - d1
print(diff.days, "divas baki")