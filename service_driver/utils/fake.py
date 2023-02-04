# -*- coding:utf-8 -*-
# @Time     :2022/6/28 20:05
# @Author   :CHNJX
# @File     :fake.py
# @Desc     :造假数据
import random
import string
import time
from datetime import datetime


class Fake:
    @classmethod
    def get_random(cls, num1, num2):
        return random.Random().randint(num1, num2)

    @classmethod
    def get_time_stamp(cls):
        return int(time.time())

    @classmethod
    def get_random_string(cls,str_len: int) -> str:
        return "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(str_len)
        )

    @classmethod
    def get_current_date(cls) -> str:
        return str(datetime.today().date())

    @classmethod
    def get_current_datetime(cls) -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

