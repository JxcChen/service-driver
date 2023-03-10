# -*- coding:utf-8 -*-
# @Time     :2023/2/7 12:38
# @Author   :CHNJX
# @File     :command.py
# @Desc     :命令工具
import subprocess
import sys
from os.path import dirname, exists
import click as click

from service_driver.har_parser import HarParser

sys.path.append(dirname(sys.path[0]))

from service_driver.project_generator import ProjectGenerator
from service_driver.swagger_generate import SwaggerGenerator

group = click.Group()


@click.command('start_project')
@click.option('-n', '--project-name', required=True, help='project name')
def start_project(project_name):
    """
    创建项目
    :param project_name: 项目名称
    """
    ProjectGenerator().project_generate(project_name)


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
    SwaggerGenerator().generate(swagger_doc, api_dir)


@click.command('run')
@click.option('-c', '--testcase',
              required=True, help='testcase')
@click.option('-t', '--tag',
              required=False, help='testcase')
@click.option('-r', '--reset', help='auto clear report', required=False, default='false',
              type=click.Choice(['true', 'false']))
def run(testcase, tag, reset):
    """
    swagger文档转换成api-object
    :param reset: auto clear report （default=False）
    :param tag: tag name
    :param testcase: testcase
    """
    command = f'pytest -v -s {testcase}'
    if reset == 'true':
        if 'win' in sys.platform:
            subprocess.call(f'rmdir /Q /S allure-results', shell=True)
        else:
            subprocess.call(f'rmdir -rf allure-results', shell=True)
    if tag:
        command += f' -m {tag}'
    subprocess.call(command + ' --alluredir=./allure-results')


@click.command('har2case')
@click.option('-h', '--har',
              required=True, help='har file path')
@click.option('-a', '--api',
              required=False, help='api object dir', default=None)
@click.option('-t', '--testcase', help='testcase dir', required=False,default='testcase')
def har2case(har, api, testcase):
    hp = HarParser(har_file_path=har,api_object=api)
    hp.generate_testcase(testcase_path=testcase)


group.add_command(start_project)
group.add_command(swagger2api)
group.add_command(run)
group.add_command(har2case)


def cmd():
    group.main()


if __name__ == '__main__':
    cmd()
