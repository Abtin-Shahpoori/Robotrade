import re
from datetime import datetime

with open("./normal.txt", "r") as f:
    dates = f.read()
f.close()

dates_arr = re.split("\n", dates)
last_month = datetime.now()
for date in dates_arr:
    real_date = date
    if date == "":
        continue
    date = datetime.strptime(date, "%Y/%m/%d")
    date = date.strftime("%m")
    date = int(date)
    if date != last_month:
        last_month = date
        print(real_date)
        

