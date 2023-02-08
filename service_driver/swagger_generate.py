# -*- coding:utf-8 -*-
# @Time     :2023/2/1 3:22 下午
# @Author   :CHNJX
# @File     :swagger_generate.py
# @Desc     :将swagger转换成api-object
import os
import sys
from os.path import dirname, exists, join

sys.path.append(dirname(sys.path[0]))

import codecs

from service_driver.loader_swagger import load_swagger
from service_driver.tenplate import Template


def generate(swagger_doc, api_dir=None):
    # root_dir = sys.path[0] if not sys.path[0].endswith(r'\venv\Scripts') else sys.path[0].replace(r'\venv\Scripts', '')
    if not api_dir:
        api_dir = 'api_object'
    if '/' not in swagger_doc and '\\' not in swagger_doc:
        swagger_doc = 'swagger/' + swagger_doc
    swagger_data = load_swagger(swagger_doc)
    _generate_template_path(swagger_data['paths'])
    tag_path_dict = _generate_template_data(swagger_data)
    template = Template()
    for tag, paths in tag_path_dict.items():
        content = template.get_content('api.tpl', tag=tag, paths=paths)
        file_path = os.path.join(api_dir, tag.lower() + '.py')
        _write(content, file_path)


def _write(content, file_path):
    dir_ = dirname(file_path)
    if not exists(dir_):
        os.makedirs(dir_)
    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(content)


def _get_method_attribute(value) -> str:
    attribute = ''
    if value.get('get'):
        attribute = 'get'
    elif value.get('post'):
        attribute = 'post'
    elif value.get('put'):
        attribute = 'put'
    elif value.get('delete'):
        attribute = 'delete'
    return attribute


def _transformation_parameters(parameters) -> list:
    return [param for param in parameters if
            param['name'] != 'raw' and param['name'] != 'root' and param['in'] != 'header']


def _transformation_json(parameters) -> list:
    json_list = []
    for param in parameters:
        if param.get('schema') and param['schema'].get('properties'):
            for key_name in param['schema']['properties'].keys():
                json_list.append(key_name)
    return json_list


def _transformation_params_list(params, json_params: list) -> list:
    params_name_list: list = [param['name'] for param in params]
    params_name_list.extend(json_params)
    return params_name_list


def _generate_url(path) -> str:
    path_name_list = path.split('/')
    if 'id' in path_name_list[-1].lower() or '{' in path_name_list[-1]:
        path_name_list.pop(-1)
    return '/'.join(path_name_list)


def _generate_name(path) -> str:
    path_name_list = path.split('/')
    return path_name_list[-2].split('?')[0] if 'id' in path_name_list[-1].lower() or '{' in path_name_list[-1] else \
        path_name_list[-1].split('?')[0]


def _generate_url_param(path):
    path_name_list: list[str] = path.split('/')
    if 'id' in path_name_list[-1].lower() or '{' in path_name_list[-1]:
        return path_name_list[-1].replace('{', '').replace('}', '')
    return ''


def _transformation_file(json_params) -> list:
    return [param for param in json_params if 'file' in param]


def _generate_template_path(swagger_paths):
    for path, value in swagger_paths.items():
        method_attribute = _get_method_attribute(value)
        value['method'] = method_attribute
        value['tag'] = value[method_attribute]['tags'][0]
        value['desc'] = value[method_attribute]['summary']
        parameters = value[method_attribute]['parameters']
        value['parameters'] = _transformation_parameters(parameters)
        value['json'] = _transformation_json(parameters)
        value['files'] = _transformation_file(value['json'])
        value['params_list'] = _transformation_params_list(value['parameters'], value['json'])
        value['url'] = _generate_url(path)
        value['name'] = _generate_name(path)
        value['url_param'] = _generate_url_param(path)


def _generate_template_data(swagger_data) -> dict:
    tag_path_dict = {}
    for tag in swagger_data['tags']:
        tag_name: str = tag['name']
        tag_name = tag_name.replace('/', '-', -1)
        tag_path_list = {name: path for name, path in swagger_data['paths'].items() if
                         path['tag'].replace('/', '-', -1) == tag_name}
        tag_path_dict[tag_name.capitalize()] = tag_path_list
    return tag_path_dict


if __name__ == '__main__':
    pass
