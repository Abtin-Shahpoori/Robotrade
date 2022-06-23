from algo import buysell 
import sys
from datetime import datetime
import re

sys.path.append("../..")
from bot_template import Bot

bot = Bot(title="buy-sell")
bot.algo = buysell
with open("../tests/test_data/normal.txt", "r") as f:
    dates = f.read()
f.close()

dates_arr = re.split("\n", dates)
for date in dates_arr:
    date = datetime.strptime(date, "%Y/%m/%d")
    date = datetime.timestamp(date)
    date = int(date)
    print(bot.test(start_time=date))
