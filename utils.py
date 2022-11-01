import hmac
import hashlib
import time

def generate_signature(query_string, secret):
    return hmac.new(
        secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256
    ).hexdigest()

def get_current_timestamp():
    return int(time.time() * 1000)