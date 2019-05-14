import json
import hashlib


# 获取加签
def get_sign(values, timestamp):
    sign_str = "ahakid9fdce5d12dea093b860e8772" + json.dumps(values, sort_keys=True) + timestamp
    sign_str = sign_str.replace(' ', '')
    sign = hashlib.md5(sign_str.encode("utf8")).hexdigest()
    return sign
