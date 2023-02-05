# from __future__ import absolute_import
# import re
# import ast
# from setuptools import setup
#
# _version_re = re.compile(r'__version__\s+=\s+(.*)')
#
# with open('service_driver/_version.py', 'rb') as f:
#     version = str(ast.literal_eval(_version_re.search(
#         f.read().decode('utf-8')).group(1)))
#
# with open('requirements.txt.txt') as f:
#     requirements = [line for line in f.read().splitlines() if line]
#
# setup(
#     name='swagger-py-codegen',
#     description='api test framework cli',
#     version=version,
#     author='CHNJX',
#     author_email='rejown@gmail.com',
#     url='https://github.com/JxcChen/service-driver',
#     packages=['service_driver'],
#     package_data={'templates': ['service_driver/templates/*']},
#     include_package_data=True,
#     entry_points={
#         'console_scripts': [
#             'swagger_py_codegen=swagger_py_codegen:generate'
#         ]
#     },
#     install_requires=requirements,
#     tests_require=['pytest'],
#
# )
