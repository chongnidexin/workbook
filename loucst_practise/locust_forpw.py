# 导包
from locust import task, HttpLocust, TaskSet

import json
import requests
import gzip
from Crypto.Cipher import ARC4


def encode(key, body, isgzip=True):
    temp_key = key.encode('utf-8')
    rc = ARC4.new(temp_key)
    data = json.dumps(body)

    if isgzip:
        en_msg = rc.encrypt(gzip.compress(data.encode('utf-8')))
    else:
        en_msg = rc.encrypt(data.encode('utf-8'))
    return en_msg


# 定义类（TaskSet任务集合）
class Work(TaskSet):

    # 定义方法
    @task(1)  # 定义任务权重（数值越大执行次数越多）
    def for_pw(self):
        req_body = {
            "db": "865256035459322",
            "dc": "a60ae7fc7f0eabf04ebfe349022ce223",
            "df": "",
            "dg": "Meizu",
            "dh": "Meizu",
            "di": "M721C",
            "dl": "",
            "dj": 24,
            "dk": "8.1.0",
            "dm": [
                {
                    "fa": "com.ss.android.ugc.aweme",
                    "fb": 81230
                },
                {
                    "fa": "com.ss.android.ugc.live",
                    "fb": 570
                },
                {
                    "fa": "com.taobao.taobao",
                    "fb": 570
                }
            ],
            "ha": "1",
            "na": "1.0",
            "ok": [
                {
                    "bb": "com.ss.android.ugc.aweme",
                    "c": "7",
                    "g": "c9ddfaa51671fb4249b392bb67d2cc43",
                    "bc": "5.0.0",
                    "bd": 500,
                    "be": "ma",
                    "bf": 0,
                    "bg": 2
                }
            ],
            "ng": "62e45913d032f80956b627ed68069934f37e7f35",
            "ni": 0,
            "nj": 1,
            "nk": 0,
            "nl": 0,
            "nm": 1566567925883,
            "no": 60000,
            "np": 0,
            "qb": 7003006,
            "qc": "7.3.6",
            "ps": "com.android.mms",
            "xg": "gO0o2CXwVIVO",
            "xk": "Flyme 7.9.5.28 beta||7|noncta|Flyme 7.9.5.28 beta",
            "pf": "1.9.002_VER_32535899255715"
        }
        # url = "http://t2-xj.antuzhi.com/fir/e/v1/pw?p=1&v=30&t=1546672087000&g=2"

        key = "2873de803723c68458c8cc905e7d97c4"
        en_body = encode(key, req_body)

        res = self.client.post(
            "/fir/e/v1/pw?p=1&v=30&t=1546672087000&g=2", data=en_body)
        print(res.status_code)


class Tadie(HttpLocust):
    task_set = Work
    min_wait, max_wait = 500, 1000
    host = "http://t2-xj.antuzhi.com"
