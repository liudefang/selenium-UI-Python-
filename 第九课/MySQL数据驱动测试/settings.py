# -*- encoding: utf-8 -*-
# @Time    : 2018/6/14 14:35
# @Author  : mike.liu
# @File    : settings.py

import os
import sys

# 主程序目录文件


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.insert(0, BASE_DIR)

from 第九课.MySQL数据驱动测试.mydb import MyDB

class Global:
    # 数据库配置目录
    db_path = os.path.join(BASE_DIR, "MySQL数据驱动测试/db.conf")

    db1 = MyDB(db_path, 'TESTDB')

