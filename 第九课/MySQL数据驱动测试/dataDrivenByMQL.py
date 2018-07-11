# -*- encoding: utf-8 -*-
# @Time    : 2018/6/12 20:33
# @Author  : mike.liu
# @File    : dataDrivenByMQL.py

# 初始化日志对象
import logging

import time
import traceback
import unittest

import ddt
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from 第九课.MySQL数据驱动测试.MyMySQL import MyMySQL

logging.basicConfig(
    # 日志级别
    level = logging.INFO,
    # 日志格式
    # 时间，代码所在文件名，代码行号，日志级别名字，日志信息
    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # 打印日志的时间
    datefmt='%a, %Y-%m-%d %H:%M:%S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    filename = 'E:\\Python\\DataDrivenProject\\report.log',
    # 打开日志文件的方式
    filemode='w'
)

def getTestDatas():
    db = MyMySQL(
        host="10.1.2.71",
        port=3306,
        dbName="testdb",
        username="root",
        password="testjfz",
        charset="utf8"
    )
    #从数据库测试表中获取测试数据
    testData = db.getDataFromDataBases()
    #关闭数据库连接
    db.closeDatabase()
    # testData = self.db1_cursor.execute()
    return testData

@ddt.ddt
class TestDemo(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path="E:\\Python36\\chromedriver")

    @ddt.data(* getTestDatas())
    def test_dataDrivenByFile(self, data):
        username, password, expectData = tuple(data)

        url = "http://10.1.2.211:8080/login.jsp"
        # 访问登录首页
        self.driver.get(url)
        # 将浏览器窗口最大化
        self.driver.maximize_window()
        print(username, password, expectData)

        # 设置隐式等待时间为10秒
        self.driver.implicitly_wait(10)

        try:

            # 找到用户名和密码输入框，并输入测试数据
            self.driver.find_element_by_xpath("//*[@name='username']").send_keys(username)
            self.driver.find_element_by_xpath("//*[@name='password']").send_keys(password)

            # 找到登录按钮，并单击
            self.driver.find_element_by_xpath("//*[@class='login-btn']").click()
            time.sleep(3)
            # 断言期望结果是否出现在页面源代码中
            self.assertTrue(expectData in self.driver.page_source)
        except NoSuchElementException as e:
            print(e)
            logging.error("查找的页面元素不存在，异常堆栈信息：" + str(traceback.format_exc()))

        except AssertionError as e:
            print(e)
            logging.info("登录'%s',期望'%s',失败" % (username, expectData))

        except Exception as e:
            print(e)
            logging.error("未知错误，错误信息：" + str(traceback.format_exc()))

        else:
            logging.info("登录'%s',期望'%s',成功" % (username, expectData))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
