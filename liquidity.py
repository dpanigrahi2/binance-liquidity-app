#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from orders import place_order, cancel_open_orders

import requests
import time

request_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
points_from_spot_price = 100 # this value can be reduced to [5-10] for testing

current_price = float(requests.get(request_url).json()['price'])
ask_price = current_price + points_from_spot_price
bid_price = current_price - points_from_spot_price
print (f'Current Price : {current_price}')
place_order('BUY', bid_price)
place_order('SELL', ask_price)

while True:
    current_price = float(requests.get(request_url).json()['price'])
    print (f'Bid Price : {bid_price} Current Price : {current_price} Ask Price : {ask_price}')
    if (bid_price < current_price < ask_price):
         pass
    else:
        '''
            current_price has reached lower/higher than bid/ask price,
            hence new bid/ask orders should be placed
        '''
        cancel_open_orders()
        place_order('BUY', current_price - points_from_spot_price)
        place_order('SELL', current_price + points_from_spot_price)
        ask_price = current_price + points_from_spot_price
        bid_price = current_price - points_from_spot_price
    time.sleep(1)


