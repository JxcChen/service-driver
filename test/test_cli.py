import os
from os.path import join, dirname

from service_driver.project_generator import project_generate
from service_driver.swagger_generate import generate


class TestProjectGenerator:
    def test_start_project(self):
        project_generate('new_project')
        assert os.path.isdir(os.path.join('new_project', "api_object"))
        assert os.path.isdir(os.path.join('new_project', "testcase"))

    def test_swagger_generate(self):
        generate(join(join(dirname(__file__), '..'), 'test/swagger/swagger.yaml'),
                 join(join(dirname(__file__), '..'), 'test/api_object'))
        assert os.path.exists(os.path.join(os.path.dirname(__file__) + "/api_object", "users2.py"))
