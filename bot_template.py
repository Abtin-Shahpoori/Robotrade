from uuid import uuid1 as uuid
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
        return 
    
    def fetch_order_book(self):
        return rq.get(self.config.order_book)

    def test(self):
        candles = rq.get("https://api.kucoin.com/api/v1/market/candles?type=1min&symbol=TRX-USDT&startAt={start_time}&endAt={start_time+86400").text
        candles = json.loads(candles)
        candles = candles["data"]

        try:
            self.algo(1, 3)
        except:
            raise RuntimeError("algo not defind")
        
        order = self.algo(1, 3)
        for candle in candles:
            print(candle)

    def balance_sheet():
        pass

