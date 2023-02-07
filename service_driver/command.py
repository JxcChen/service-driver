# -*- coding:utf-8 -*-
# @Time     :2023/2/7 12:38
# @Author   :CHNJX
# @File     :command.py
# @Desc     :命令工具
import sys
from os.path import dirname, exists
import click as click
sys.path.append(dirname(sys.path[0]))

import os
from service_driver.project_generator import create_folder, create_file, generate_base_need
from service_driver.swagger_generate import generate

group = click.Group()


@click.command('start_project')
@click.option('-n', '--project-name', required=True, help='project name')
def start_project(project_name):
    """
    创建项目
    :param project_name: 项目名称
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


@click.command('swagger2api')
@click.option('-s', '--swagger-doc',
              required=True, help='Swagger doc file.')
@click.option('-d', '--api-dir',
              required=False, help='api save dir.')
def swagger2api(swagger_doc, api_dir):
    """
    swagger文档转换成api-object
    :param swagger_doc: swagger.json 文件
    :param api_dir:  api存放路径 非必填
    """
    generate(swagger_doc, api_dir)


group.add_command(start_project)
group.add_command(swagger2api)


def cmd():
    group.main()


if __name__ == '__main__':
    cmd()
