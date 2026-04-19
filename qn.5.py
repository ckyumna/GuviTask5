from datetime import datetime

#creating a datetime object
dt = datetime.now()

#extracting year, month and day using lambda function
date = lambda d : (d.year, d.month, d.day)

print(date(dt))
