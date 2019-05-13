# -*- coding: UTF-8 -*-
import requests

test = requests.get('http://www.baidu.com')

print(test.text)
