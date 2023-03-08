# -*- coding:utf-8 -*-
# @Time     :2023/2/2 10:41 下午
# @Author   :CHNJX
# @File     :project_generator.py
# @Desc     :项目创造器

import sys
from os import listdir, makedirs
from os.path import dirname, exists, join

sys.path.append(dirname(sys.path[0]))

from service_driver.tenplate import Template
from service_driver import sd_utils


class ProjectGenerator:
    def project_generate(self, project_name):
        """
        创建项目
        :param project_name: 项目名称
        :return: None
        """
        if exists(project_name):
            print(f'project {project_name} is already existed')
            return 1
        sd_utils.create_folder(project_name)
        sd_utils.create_folder(join(project_name, 'testcase'))
        sd_utils.create_folder(join(project_name, 'swagger'))
        sd_utils.create_folder(join(project_name, 'har'))
        sd_utils.create_folder(join(project_name, 'api_object'))
        for dir_name in listdir(project_name):
            if dir_name == 'swagger':
                continue
            cur_dir = join(project_name + '/' + dir_name, '__init__.py')
            sd_utils.create_file(cur_dir)
        self.__generate_base_need(project_name)

    def __generate_base_need(self, project_name):
        template = Template()
        api_object_dir = join(project_name, 'api_object')
        testcase_dir = join(project_name, 'testcase')
        sd_utils.write(template.get_content('base_api.tpl'), join(api_object_dir, 'base_api.py'))
        sd_utils.write(template.get_content('api_demo.tpl'), join(api_object_dir, 'api_demo.py'))
        sd_utils.write(template.get_content('base_testcase.tpl'), join(testcase_dir, 'test_base.py'))
        sd_utils.write(template.get_content('testcase_demo.tpl'), join(testcase_dir, 'testcase_demo.py'))
        sd_utils.write(swagger_json, join(f'{project_name}/swagger', 'swagger_demo.json'))


swagger_json = r"""
{
  "swagger": "2.0",
  "info": {
    "version": "1.0.0",
    "title": "Sample API",
    "description": "A sample API for demonstration purposes",
    "contact": {
      "name": "Your Name",
      "email": "youremail@example.com"
    }
  },
  "host": "api.example.com",
  "basePath": "/v1",
  "schemes": [
    "http"
  ],
  "tags": [
    {
      "name": "users",
      "description": "Operations related to users"
    }
  ],
  "paths": {
    "/users": {
      "get": {
        "tags": [
          "users"
        ],
        "summary": "Get a list of users",
        "description": "Returns a list of all users in the system",
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "Successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/User"
              }
            }
          },
          "default": {
            "description": "Error response",
            "schema": {
              "$ref": "#/definitions/Error"
            }
          }
        }
      }
    },
    "/users/{userId}": {
      "get": {
        "tags": [
          "users"
        ],
        "summary": "Get a user by ID",
        "description": "Returns the user with the specified ID",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "userId",
            "in": "path",
            "description": "The ID of the user to retrieve",
            "required": true,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful operation",
            "schema": {
              "$ref": "#/definitions/User"
            }
          },
          "default": {
            "description": "Error response",
            "schema": {
              "$ref": "#/definitions/Error"
            }
          }
        }
      }
    }
  },
  "definitions": {
    "User": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "email": {
          "type": "string"
        }
      }
    },
    "Error": {
      "type": "object",
      "properties": {
        "message": {
          "type": "string"
        },
        "code": {
          "type": "integer"
        }
      }
    }
  }
}
"""

if __name__ == '__main__':
    pass
