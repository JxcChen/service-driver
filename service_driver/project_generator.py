# -*- coding:utf-8 -*-
# @Time     :2023/2/2 10:41 下午
# @Author   :CHNJX
# @File     :project_generator.py
# @Desc     :项目创造器

import sys
from os.path import dirname, exists

sys.path.append(dirname(sys.path[0]))

import click as click
from jinja2 import FileSystemLoader, Environment

import os

group = click.Group()


# @click.command('start')
# @click.option('-n', '--project-name', required=True, help='project name')
def start_project(project_name):
    """
    创建项目
    :param project_name: 项目名称
    :return: None
    """
    if exists(project_name):
        print(f'project {project_name} is already existed')
        return 1
    create_folder(project_name)
    create_folder(os.path.join(project_name, 'testcase'))
    create_folder(os.path.join(project_name, 'api_object'))
    for dir_name in os.listdir(project_name):
        cur_dir = os.path.join(project_name + '/' + dir_name, '__init__.py')
        create_file(cur_dir)
    generate_base_need(project_name)


def create_folder(path):
    os.makedirs(path)
    print(f'create folder {path}')


def create_file(file_path, file_content=""):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"created file: {file_path}")


def generate_base_need(project_name):
    template = Template()
    api_object_dir = os.path.join(project_name, 'api_object')
    testcase_dir = os.path.join(project_name, 'testcase')
    _write(template.get_content('base_api.tpl'), os.path.join(api_object_dir, 'base_api.py'))
    _write(template.get_content('api_demo.tpl'), os.path.join(api_object_dir, 'api_demo.py'))
    _write(template.get_content('base_testcase.tpl'), os.path.join(testcase_dir, 'test_base.py'))
    _write(template.get_content('testcase_demo.tpl'), os.path.join(testcase_dir, 'testcase_demo.py'))


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
    group.main()
