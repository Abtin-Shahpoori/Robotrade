from algo import buysell 
import sys
from datetime import datetime, date

sys.path.append("../..")
from bot_template import Bot

bot = Bot(title="buy-sell")
bot.algo = buysell

print(bot.test(start_time=1556150400))
