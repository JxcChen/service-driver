# -*- coding:utf-8 -*-
# @Time     :2023/2/3 4:10 下午
# @Author   :CHNJX
# @File     :test_base.py
# @Desc     :
import os

from service_driver.utils.database_conn import DatabaseConn
from service_driver.utils.service_logger import Logger
from service_driver.base_testcase import BaseTestcase


class TestBase(BaseTestcase):
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    logger = Logger.getLogger("testcase", base_dir)

    # 需要先获取数据库配置
    # database = DatabaseConn(sql_config)

