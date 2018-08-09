import time
import datetime

#year, month, day, hour, minute, second
birthday = datetime.datetime(1981, 3, 31)
from datetime import datetime

age = datetime.today() - birthday 
print(age)

#year, month, day, hour, minute, second
my_bday = datetime.date(1981, 3, 31, 10, 15, 0)
bday_days = (datetime.date.now()  - my_bday)

bday_years = bday_days.days / 365

print("I am " + bday_years + " years old!") 


