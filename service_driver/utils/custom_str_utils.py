# -*- coding:utf-8 -*-
# @Time     :2022/6/29 17:12
# @Author   :CHNJX
# @File     :custom_str_utils.py
# @Desc     :字符串的自定义方法
import random
import re
from service_driver.utils.service_logger import Logger


class CustomStrUtils:
    logger = Logger.getLogger("testcase")

    @classmethod
    def get_random_num(cls, formal_str):
        """
        获取随机数占位符的范围
        """
        if "random" not in formal_str:
            cls.logger.info('没有找到占位符')
            return 0

        # 匹配上 random中的范围
        try:
            random_range = re.match(r'.*{random\((.*?)\)}', formal_str, flags=0).group(1)
            return int(random_range)
        except Exception as e:
            cls.logger.error('随机数占位符格式错误')
            return 0
