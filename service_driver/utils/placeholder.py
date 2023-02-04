# -*- coding:utf-8 -*-
# @Time     :2022/6/29 10:55
# @Author   :CHNJX
# @File     :placeholder.py
# @Desc     :形参占位符转成实参
from service_driver.utils.service_logger import Logger

PLACEHOLDER_PREFIX = '${'
PLACEHOLDER_SUFFIX = '}'


class Placeholder:
    # 声明占位符的前后缀
    logger = Logger.getLogger('testcase')

    @classmethod
    def resolve_str(cls,text: str, parameter: dict):
        """
        转换字符串中携带的占位符
        """
        if parameter is None or len(parameter) == 0 or text is None or text == '':
            return text
        start_index = text.find(PLACEHOLDER_PREFIX)
        while start_index != -1:
            end_index = text.find(PLACEHOLDER_SUFFIX, start_index + len(PLACEHOLDER_PREFIX))
            if end_index != -1:
                formal = text[start_index + len(PLACEHOLDER_PREFIX):end_index]
                next_index = end_index + len(PLACEHOLDER_SUFFIX)
                try:
                    actual = str(parameter[formal])
                    if actual:
                        # 替换占位符
                        text = text.replace('${'+formal+'}', actual)
                        next_index = start_index + len(actual)
                    else:
                        cls.logger.info("Could not resolve placeholder '" + formal + "' in [" + text + "] ")
                except Exception as e:
                    cls.logger.error(
                        "Could not resolve placeholder '" + formal + "' in [" + text + "]: " + e.__str__())
                start_index = text.find(PLACEHOLDER_PREFIX, next_index)
            else:
                start_index = -1
        return text

    @classmethod
    def resolve_dict(cls, dic: dict, parameter: dict):
        """替换字典中值的占位符"""
        if parameter is None or len(parameter) == 0 or dic is None or len(dic) == 0:
            return dic
        res = {}
        for key, value in dic.items():
            if PLACEHOLDER_PREFIX in value:
                res[key] = cls.resolve_str(value, parameter)
        return res
