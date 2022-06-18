def buysell(**rishe):
    lastprice, check, a, b, c, pretet, coins, price, cnt, vaziyat, delay = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    tethers, maxx = 100, 100

    while True:
        current_price = int(rishe.get("current_price"))
        tethers = float(rishe.get("tether"))

        candle = rishe.get("candle")
        shoro = float(candle[len(candle) - 1][1])
        payan = float(candle[len(candle) - 1][2])
        a = payan - ((payan - shoro) / 60)
        b = payan
        
        if tethers != 0: #kharid
            if b <= a and b < current_price:
                time.sleep(1)
                return 1
            else: 
                return 0
    
        else: #forosh
            return {"entery_price": current_price + (current_price/1000), "stop_lost": current_price - 3*(current_price/100), "take_profit": current_price}
