# -*- encoding: utf-8 -*-
# @Time    : 2017/12/20 18:02
# @Author  : mike.liu
# @File    : run_all_case.py
import smtplib
import unittest

import os

import time




#发送邮箱服务器
from email.header import Header
from email.mime.text import MIMEText

#用例路径
case_path = os.path.join(os.getcwd(),"testcase")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)

    print("discover")

    return discover

if __name__ == '__main__':
    #unittest.main()       #启动单元测试
    runner = unittest.TextTestRunner()
    runner.run(all_case())   #运行测试用例

