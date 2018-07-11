# -*- encoding: utf-8 -*-
# @Time    : 2018/6/14 15:03
# @Author  : mike.liu
# @File    : mydb.py
import configparser

import mysql.connector


class MyDB:
    def __init__(self, config_file, db):
        config = configparser.ConfigParser()

        # 从服务器读取域名，端口，用户名，密码
        config.read(config_file, encoding='utf-8')
        self.host = config[db]['host']
        self.port = config[db]['port']
        self.user = config[db]['username']
        self.passwd = config[db]['password']
        self.db_name = config[db]['dbName']
        self.charset = config[db]['charset']

    def get_conn(self):

        try:
            self.dbconn = mysql.connector.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db_name=self.db_name, charset=self.charset)
        except Exception as e:
            print("连接数据库失败:%s" % e)
            exit()

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_dbconn(self):
        return self.dbconn

    def select_one_record(self, query):
        '''返回结果只包含一条记录'''
        print("query:%s" %(query))
        try:
            db_cursor = self.dbconn.cursor()
            db_cursor.execute(query)

            query_result = db_cursor.fetchone()
            self.dbconn.commit()
            self.dbconn.close()
            return (query_result, True)
        except Exception as e:
            print("执行数据库查询操作失败,%s" % e)
            self.dbconn.close()
            return (e, False)

    def select_many_record(self, query):
        '''返回多条数据'''
        print("query:%s" % query)
        try:
            db_cursor = self.dbconn.cursor()
            db_cursor.execute(query)

            query_result = db_cursor.fetchall()
            self.dbconn.commit()
            self.dbconn.close()
            return (query_result, True)
        except Exception as e:
            print("执行查询数据库失败，%s" % e)
            self.dbconn.close()
            return (e, False)

    def close(self):
        self.dbconn.close()








