# -*- coding:utf-8 -*-
# @Time     :2022/7/1 11:20
# @Author   :CHNJX
# @File     :database_conn.py
# @Desc     :获取数据库链接

import pymysql
from service_driver.utils.service_logger import Logger


class DatabaseConn:
    conn = ''
    cursor = ''
    logger = Logger.getLogger('testcase')
    def __init__(self, database_config):
        """
        :param database_config:
            example:
            database_config = {
                'host': 'xxx.cn',
                'port': 3306,
                'user': 'root',
                'password': '123456',
                'database': 'test',
                'autocommit': True
            }
        """
        self.create_conn(database_config)

    def create_conn(self, database_config):
        if not self.conn:
            self.conn = pymysql.connect(charset='utf8', **database_config)
            self.cursor = self.conn.cursor()

    def close_conn(self):
        if self.conn:
            self.conn.close()

    def excuse_sql(self, sql_str, params=None):
        self.conn.ping(reconnect=True)
        self.cursor.execute(sql_str, params)
        self.logger.info('执行sql语句: ' + sql_str)
        # 判断是否为查询语句
        if 'select' in sql_str:
            return self.cursor.fetchone()
        else:
            self.conn.commit()
            return self.cursor.fetchone()
