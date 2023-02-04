# -*- coding:utf-8 -*-
# @Time     :2023/2/3 4:14 下午
# @Author   :CHNJX
# @File     :testcase_demo.py
# @Desc     :
from service_driver.test_base import TestBase


class TestDemo(TestBase):

    def test01(self):
        self.logger.info('aaaaa')
        self.replace_formal_str_2_actual('${randomaaa')
        assert 1 == 1
