# -*- coding:utf-8 -*-
# @Time     :2023/2/2 10:41 下午
# @Author   :CHNJX
# @File     :project_generator.py
# @Desc     :项目创造器
from os.path import dirname, exists

from jinja2 import FileSystemLoader, Environment

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TESTCASE_DIR = os.path.join(BASE_DIR, 'testcase')
API_OBJECT_DIR = os.path.join(BASE_DIR, 'api_object')


def start_project(project_name):
    """
    创建项目
    :param project_name: 项目名称
    :return: None
    """
    if not exists(TESTCASE_DIR):
        os.mkdir(TESTCASE_DIR)
    if not exists(API_OBJECT_DIR):
        os.mkdir(API_OBJECT_DIR)
    for dir_name in os.listdir(BASE_DIR):
        cur_dir = os.path.join(BASE_DIR, dir_name)
        with open(os.path.join(cur_dir, '__init__.py'), 'w') as file:
            pass
    generate_base_need()


def generate_base_need():
    template = Template()
    _write(template.get_content('base_api.tpl'), os.path.join(API_OBJECT_DIR, 'base_api.py'))
    _write(template.get_content('base_testcase.tpl'), os.path.join(TESTCASE_DIR, 'test_base.py'))


def _write(content, file_path):
    dir_ = dirname(file_path)
    if not exists(dir_):
        os.makedirs(dir_)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


class Template:
    def __init__(self):
        loader = FileSystemLoader(os.path.join(
            os.path.dirname(__file__), 'templates'))
        self.env = Environment(loader=loader)

    def get_content(self, tpl_name, **kwargs):
        return self.env.get_template(tpl_name).render(**kwargs)



if __name__ == '__main__':
    start_project('ss')
