# -*- coding:utf-8 -*-
# @Time     :2023/3/1 11:08
# @Author   :CHNJX
# @File     :sd_utils.py
# @Desc     :public utils
from urllib.parse import unquote


def covert_list_to_dict(list_data):
    """
    将har list data 转换成dict
    :param list_data
        list_data (list)
            [
                {"name": "v", "value": "1"},
                {"name": "w", "value": "2"}
            ]

        Returns:
            dict:
                {"v": "1", "w": "2"}
    """
    return {item['name']: item.get('value') for item in list_data}


def convert_x_www_form_to_dict(form_data: str):
    """
    将form表单数据装换成dict字典数据
    :param form_data:  (str): a=1&b=2
    :return: (dict) {"a":1, "b":2}
    """
    if isinstance(form_data, str):
        res_dict = {}
        for kev_value in form_data.split('&'):
            try:
                key, value = kev_value.split('=')
            except ValueError:
                raise Exception(f"错误的 x_www_form_urlencoded 数据: {form_data}")
            # unquote('abc%20def') -> 'abc def'.
            res_dict[key] = unquote(value)
        return res_dict
    else:
        return form_data
