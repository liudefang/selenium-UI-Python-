# -*- encoding: utf-8 -*-
# @Time    : 2018/6/13 11:07
# @Author  : mike.liu
# @File    : DataBaseInit.py

import pymysql


class DataBaseInit(object):
    # 本类用于完成初始化数据操作
    # 创建数据库，创建数据表，向表中插入测试数据
    def __init__(self ,host, port, dbName, username, password, charset):
        self.host = host
        self.port = port
        self.db = dbName
        self.user = username
        self.passwd = password
        self.charset = charset

    def insertDatas(self):
        try:
            # 连接mysql数据库中具体某个库
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                db=self.db,
                passwd=self.passwd,
                charset=self.charset
            )
            cur = conn.cursor()
            # 向测试表中插入测试数据
            sql = "insert into testdata(Movie_Name,Movie_Property, Excpect_result) values(%s,%s, %s);"
            res = cur.executemany(sql,[('defang1', '123', '德芳理财'),('defang2', '123', '德芳客服'),('defang3', '123', '德芳运维')])
        except pymysql.Error as e:
            raise e
        else:
            conn.commit()
            print(u'初始数据插入成功')
            # 确认插入数据成功
            cur.execute("select * from testdata;")
            for i in cur.fetchall():
                print(i[0], i[1], i[2])
            cur.close()
            conn.close()

if __name__ == '__main__':
    db = DataBaseInit(
        host="192.168.159.128",
        port=3306,
        dbName="test_db",
        username="testpython",
        password="testpython",
        charset="utf8"
    )
    # db.create()
    db.insertDatas()
    print(u"数据库初始化结束")
