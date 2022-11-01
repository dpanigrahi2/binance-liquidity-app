#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import hmac
import hashlib
import time

def generate_signature(query_string, secret):
    """get HMAC with secret and query string"""
    return hmac.new(
        secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256
    ).hexdigest()

def get_current_timestamp():
    """get current epoch timestamp"""
    return int(time.time() * 1000)