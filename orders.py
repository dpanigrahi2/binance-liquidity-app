#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
from utils import generate_signature
from utils import get_current_timestamp

import requests
import os

load_dotenv()

secret = os.getenv('SECRET_KEY')
api_key = os.getenv('API_KEY')
base_url = 'testnet.binance.vision'
url_path_place_order = '/api/v3/order'
url_path_cancel_open_orders = '/api/v3/openOrders'
quantity = '0.01'
symbol = 'BTCUSDT'
order_type = 'LIMIT'
order_validity = 'GTC'

def place_order(action, price):
    query_params = f'symbol={symbol}&side={action}&type={order_type}&timeInForce={order_validity}&quantity={quantity}&price={price}&timestamp={get_current_timestamp()}'
    signature = generate_signature(query_params, secret)
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-MBX-APIKEY': api_key
    }
    url = f'https://{base_url}{url_path_place_order}?{query_params}&signature={signature}'
    response = requests.request("POST", url, headers=headers, data=payload)
    print (response.json())

def cancel_open_orders():
    query_params = f'symbol={symbol}&timestamp={get_current_timestamp()}'
    signature = generate_signature(query_params, secret)
    url = f'https://{base_url}{url_path_cancel_open_orders}?{query_params}&signature={signature}'
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-MBX-APIKEY': api_key
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.json())

