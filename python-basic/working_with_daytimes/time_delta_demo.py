from datetime import datetime, timedelta


d1=datetime(2022,4,13)
d2=datetime.now()

duration= d2 - d1

print(duration.days)
print(duration)


