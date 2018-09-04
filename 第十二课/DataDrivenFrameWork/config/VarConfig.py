# -*- encoding: utf-8 -*-
# @Time    : 2018/8/6 18:04
# @Author  : mike.liu
# @File    : VarConfig.py
import os


# 获取当前文件所在目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath = parentDirPath + "\\config\\PageElementLocator.ini"

# 获取数据文件存放绝对路径
dataFilePath = parentDirPath + "\\testdata\\erp数据驱动自动化.xlsx"

# 登录账号工作表中，每列对应的数字序号
account_username = 2
account_password = 3
account_dataBook = 4
account_isExecute = 5
account_testResult = 6

# 添加客户信息工作表中，每列对应的数字序号
customer_customerUserName = 2
customer_customerPhoneNumber = 3
customer_contactKeyWords = 4
customer_isExecute = 5
customer_runTime = 6
customer_testResult = 7
