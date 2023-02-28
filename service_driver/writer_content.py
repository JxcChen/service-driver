# -*- coding:utf-8 -*-
# @Time     :2023/2/28 18:47
# @Author   :CHNJX
# @File     :writer_content.py
# @Desc     :
import os


def write(content, file_path):
    dir_ = os.path.dirname(file_path)
    if not os.path.exists(dir_):
        os.makedirs(dir_)
    with open(file_path, 'w', 'utf-8') as f:
        f.write(content)
