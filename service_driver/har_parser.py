# -*- coding:utf-8 -*-
# @Time     :2023/2/28 18:30
# @Author   :CHNJX
# @File     :har_parser.py
# @Desc     :
import logging
import os
from service_driver.writer_content import write
from service_driver.tenplate import Template


class HarParser:

    def __init__(self, har_file_path, exclude_url):
        self.har_file = har_file_path
        self.exclude = exclude_url

    def generate_testcase_steps(self, fmt_version) -> dict:
        """
        封装测试用例步骤
        :param fmt_version:
        :return:
        """
        ...

    def _make_testcase(self, fmt_version: str) -> str:
        """
        :param fmt_version: 用例版本
        :return: 通过模板对用例转换后的内容
        """
        # 先把需要的用例步骤进行解析
        testcase_steps = self.generate_testcase_steps(fmt_version)
        temp = Template()
        return temp.get_content('har2case.tpl', **testcase_steps)

    def generate_testcase(self, fmt_version: str = 'v1'):
        """
        将har文件转换成测试用例
        :param fmt_version: 用例版本
        """
        # 1 先获取文输出文件名
        # 切割文件和扩展名
        har_file_dir = os.path.splitext(self.har_file)[0]
        testcase_file_name = f'{har_file_dir}.py'
        logging.info('开始转换测试用例')
        testcase_content = self._make_testcase(fmt_version)
        write(testcase_content, testcase_file_name)
        logging.info(f'完成{har_file_dir}的用例转换')
