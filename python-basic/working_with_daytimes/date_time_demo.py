from datetime import datetime

dt=datetime(2022,1,1)

# print(dt)
#
# now=datetime.now()
# print(now)

# https://docs.python.org/3/library/datetime.html
dt1=datetime.strptime("2022-01-01","%Y-%m-%d")
print(dt1)

import time

time_convert =time.time()
print(time_convert)

dt=datetime.fromtimestamp(time.time())
print(dt)

print(dt.year)
print(dt.month)

dt.strftime("%Y")
