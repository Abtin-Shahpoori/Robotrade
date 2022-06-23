import requests as rq
from termcolor import colored
import json
from datetime import datetime
from time import sleep

start_time = 1546300800 # timestamp 2019/1/1
todays_date = 1652659200 # timestamp 2022/06/16
precent_diff_sm = 0
n = 1
high_low_precent_sm = 0



while start_time < todays_date:
    data = rq.get(f"https://api.kucoin.com/api/v1/market/candles?type=1day&symbol=TRX-USDT&startAt={start_time}&endAt={start_time + 86401}").text
    data = json.loads(data)
    date = datetime.fromtimestamp(start_time).strftime("%Y/%m/%d")
    try:
        data = data["data"]
    except:
        sleep(10)
        start_time -= 86400
        continue

    try:
        data = data[0]
    except:
       print("No data available")
       print("----------------------------------")
       start_time += 86400
       continue

    high_diff_low = float(data[3]) - float(data[4])
    high_low_precent = (high_diff_low / float(data[3])) * 100

    if float(data[1]) > float(data[2]): # opening price is lower than the closing price so, red
        price_diff = float(data[1]) - float(data[2])
        precent_diff = (price_diff / float(data[1])) * 100
    else: 
        price_diff = float(data[2]) - float(data[1])
        precent_diff = (price_diff / float(data[2])) * 100

    if abs(precent_diff - 3.6) <= 1.5 and abs(high_low_precent - 8) <= 1.5:
        with open("./normal.txt", "a") as file:
            file.write(f"{date}\n")
        file.close()

    print(price_diff)
    print(data)

    print(datetime.fromtimestamp(start_time))
    print('----------------------------------')
    start_time += 86400
    high_low_precent_sm += high_low_precent
    precent_diff_sm += precent_diff
    n += 1

print("average open close diffrence", precent_diff_sm / n)
print("average high low diffrence", high_low_precent_sm / n)
