from uuid import uuid1 as uuid
import random
from time import sleep
from datetime import datetime
import requests as rq
import hashlib
import json

hasher = hashlib.sha256()

class Bot():
    def __init__(self, title):
        hasher.update(bytes(f"{uuid()}", 'utf-8'))
        self.__id = hasher.hexdigest()
        self.__title = title
        self.config = {}

    def gets_id(self):
        return self.__id

    def place_order(self, amount):
        pass
    
    def __fetch_current_price(self):
        prices = rq.get("https://api.kucoin.com/api/v1/market/histories?symbol=TRX-USDT").text
        prices = json.loads(prices)
        prices = prices["data"][0]
        price = float(prices["price"])
        return price

    def test(self, **args):
        start_time = int(args.get("start_time")) or int(datetime.timestamp(datetime.now()) - 86400)
        try:
            candles = rq.get(f"https://api.kucoin.com/api/v1/market/candles?type=1min&symbol=TRX-USDT&startAt={start_time}&endAt={start_time+86400}").text
        except:
            sleep(5) 
            candles = rq.get(f"https://api.kucoin.com/api/v1/market/candles?type=1min&symbol=TRX-USDT&startAt={start_time}&endAt={start_time+86400}").text

        try:
            candles = candles["data"]
        except:
            sleep(100)
            candles = rq.get(f"https://api.kucoin.com/api/v1/market/candles?type=1min&symbol=TRX-USDT&startAt={start_time}&endAt={start_time+86400}").text
            candles = json.loads(candles)
            candles = candles["data"]

        for candle in candles:
            for i, data in enumerate(candle):
                candle[i] = float(candle[i])
                
        # candles = candles["data"]
        tether_ammount = args.get("tether_ammount") or 100
        try:
            self.algo(candle=candles) 
        except:
            raise RuntimeError("algo not defind")

        candle = {}
        next_day = start_time + 86400
        profit = 0
        while start_time < next_day:
            try:
                candles = rq.get(f"https://api.kucoin.com/api/v1/market/candles?type=1min&symbol=TRX-USDT&startAt={start_time}&endAt={start_time+86400}").text
            except:
                sleep(5) 
                continue

            try:
                candles = json.loads(candles)
            except:
                print("HELLO")
            
            try:
                candles = candles["data"]
            except:
                continue

            order = self.algo(candle=candles)
            if order == 0:
                start_time += 60
                continue


            for cndl in candles:
                candle["highest"] = float(cndl[3])
                candle["lowest"] = float(cndl[4])
                start_time += 60
                if candle["highest"] < float(order["take_profit"]) and float(candle["lowest"]) > float(order["stop_loss"]):
                    rand = random.randint(1, 2)
                    if rand == 1:
                        profit = order["take_profit"] * (-1 * (tether_ammount / order["entry_price"]) + (tether_ammount / order["take_profit"]))
                    if rand == 2:
                        profit = order["stop_loss"] * (-1 * (order["entry_price"] * tether_ammount) + (order["stop_loss"] * tether_ammount))

                    tether_ammount += profit
                    break

                if candle["highest"] < order["take_profit"]:
                    profit = order["take_profit"] * (-1 * (tether_ammount / order["entry_price"]) + (tether_ammount / order["take_profit"]))
                    tether_ammount += profit
                    break
                if candle["lowest"] > order["stop_loss"]:
                    profit = order["stop_loss"] * (-1 * (tether_ammount / order["entry_price"]) + (tether_ammount / order["stop_loss"]))
                    tether_ammount += profit
                    # print(profit)
                    break

        if (tether_ammount - 100) == 0:
            return "FUCK"
        return tether_ammount

    def balance_sheet():
        pass
