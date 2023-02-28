# -*- coding:utf-8 -*-
# @Time     :2022/6/28 20:05
# @Author   :CHNJX
# @File     :fake.py
# @Desc     :造假数据
import random
import string
import time
from datetime import datetime

from faker import Faker


class Fake:
    fake = Faker(locale="zh-CN")

    @classmethod
    def get_range_random(cls, num1, num2):
        return random.Random().randint(num1, num2)

    @classmethod
    def get_random_int(cls, num):
        num1 = 1 * (num - 1)
        num2 = int('9' * num)
        return random.Random().randint(num1, num2)

    @classmethod
    def get_time_stamp(cls):
        return int(time.time())

    @classmethod
    def get_random_string(cls, str_len: int) -> str:
        return "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(str_len)
        )

    @classmethod
    def get_current_date(cls) -> str:
        return str(datetime.today().date())

    @classmethod
    def get_current_datetime(cls) -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_random_name(self):
        """
        获取随机中文名
        :return:
        """
        return self.fake.name()

    def get_random_phone(self):
        """获取随机手机号"""
        return self.fake.phone_number()

    def get_random_ssn(self):
        """获取随机身份证号"""
        return self.fake.ssn()

    def get_random_credit_card_number(self):
        """获取随机银行卡号"""
        return self.fake.credit_card_number()

    def get_random_address(self):
        """获取随机地址"""
        return self.fake.address().split(' ')[0]

    def get_random_email(self):
        """获取随机邮箱"""
        return self.fake.email()

    def get_random_date(self):
        """获取随机日期"""
        return self.fake.date()

    def get_random_this_year_date(self):
        """获取今年随机日期"""
        return self.fake.date_this_year()

    def get_random_date_time(self):
        """获取随机时间"""
        return self.fake.date_time()

    def get_random_this_year_date_time(self):
        """获取随机时间"""
        return self.fake.date_time_this_year()

    def get_random_future_date(self):
        """获取未来的日期"""
        return self.fake.future_date()

    def get_random_future_date_time(self):
        """获取未来的日期"""
        return self.fake.future_datetime()

    def get_customer_date(self, start_date: str, end_date: str):
        """
        获取自定义范围的日期
        :param start_date:  开始时间 1y为往后一年  -1y为往前一年
        :param end_date:  结束时间
        :return:
        """
        return self.fake.date_between(start_date=start_date, end_date=end_date)

    def get_customer_date_time(self, start_date: str, end_date: str):
        """
        获取自定义范围的时间
        :param start_date:  开始时间 +1y为往后一年  -1y为往前一年
        :param end_date:  结束时间
        :return:
        """
        return self.fake.date_time_between(start_date=start_date, end_date=end_date)
