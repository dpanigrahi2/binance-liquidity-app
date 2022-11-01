#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from orders import place_order, cancel_open_orders

import requests
import time

request_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
points_from_spot_price = 100

current_price = float(requests.get(request_url).json()['price'])
ask_price = current_price + points_from_spot_price
bid_price = current_price - points_from_spot_price
place_order('BUY', bid_price)
place_order('SELL', ask_price)

while True:
    current_price = float(requests.get(request_url).json()['price'])
    if (bid_price <= current_price <= ask_price):
        pass
    else:
        cancel_open_orders()
        place_order('BUY', current_price - points_from_spot_price)
        place_order('SELL', current_price + points_from_spot_price)
        ask_price = current_price + points_from_spot_price
        bid_price = current_price - points_from_spot_price
    time.sleep(1)

