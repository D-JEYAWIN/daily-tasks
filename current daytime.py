import datetime

x = datetime.datetime(2022, 9, 15,9,45,45,566)
date_time= datetime.datetime.now()
print(date_time)
print(x)
print(x.strftime("%B"))
print(x.strftime("%A"))
print(x.strftime("%a"))