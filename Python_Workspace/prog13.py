#1>
#format of printing
import datetime
print datetime.datetime.today()
#2>
#format of printing
from datetime import datetime
print datetime.today()
#3>
#adding to date
from datetime import datetime, timedelta
new_date = datetime.today()
new_date = new_date + timedelta(days=3)
print new_date
#4>
#time formating in python
from datetime import datetime
time = datetime.today()
print time.strftime("%a, %d %b %Y, %I %M %p ")
time = time + timedelta(days=3,minutes=3)
print time.strftime("%a, %d %b %Y, %I %M %p ")