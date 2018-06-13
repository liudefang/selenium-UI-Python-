# -*- encoding: utf-8 -*-
# @Time    : 2018/6/12 20:02
# @Author  : mike.liu
# @File    : MyMySQL.py
import pymysql

class MyMySQL(object):
    def __init__(self, host, port, dbName, username,password, charset):
        # 进行数据库初始化
       # dbInit = DataBaseInit(host, port, dbName, username, password, charset)
        self.conn = pymysql.connect(
            host=host,
            port=port,
            db=dbName,
            user=username,
            passwd=password,
            charset=charset

        )
        self.cur = self.conn.cursor()

    def getDataFromDataBases(self):
        # 从testdb表中获取需要的测试数据
        # Movie_name作为用户名，Movie_property作为密码，excpect_result作为预期结果
        self.cur.execute("select Movie_Name,Movie_Property,Excpect_result from testdata; ")
        # 从查询预期取回所有查询结果
        datasTuple = self.cur.fetchall()
        return datasTuple

    def closeDatabase(self):
        # 数据库后期清理工作
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    db = MyMySQL(
        host="10.1.2.71",
        port=3306,
        dbName="testdb",
        username="root",
        password="testjfz",
        charset="utf8"
    )
    print(db.getDataFromDataBases())
    db.closeDatabase()