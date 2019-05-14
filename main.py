# -*- coding: UTF-8 -*-
import requests
import time
import sign

t = time.time()
timestamp = str(int(t))

values = {
    'type': "3",
    'order_uuid': 'ACF51F7823504CEDBDE3FE3EFB96133B',
}
url = "https://mktapi-test3.d.ahaschool.com/mall/orders/pay"

sign = sign.get_sign(values, timestamp)
headers = {
    'clientid': "1",
    'sign': sign,
    'timestamp': timestamp
}
res = requests.post(url, data=values, headers=headers)

print(res.text)


