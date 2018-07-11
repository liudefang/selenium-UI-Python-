# -*- encoding: utf-8 -*-
# @Time    : 2018/7/5 19:52
# @Author  : mike.liu
# @File    : CaseLoginTest.py
import traceback
import unittest

import time

import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from 第十课.login import driver
from 第十课.数据驱动.pageObject.LoginPage import LoginPage


class CaseLoginTest(unittest.TestCase):
    def setUp(self):

        driver = webdriver.Chrome(executable_path="E:\\Python36\\chromedriver")

    def test_login1(self):


        login = LoginPage(driver)

        try:

            # 找到用户名和密码输入框，并输入测试数据
            login.userNameObj().send_keys("defang1")
            login.passwordObj().send_keys("123")

            # 找到登录按钮，并单击
            login.loginButton().click()
            time.sleep(3)
            # 断言期望结果是否出现在页面源代码中
            # self.assertTrue("德芳理财" in assert_string_in_pagesource())
        except NoSuchElementException as e:
            print(e)
            logging.error("查找的页面元素不存在，异常堆栈信息：" + str(traceback.format_exc()))

        except AssertionError as e:
            print(e)
            logging.info("登录'%s',期望'%s',失败" % ("defang1", "德芳理财"))

        except Exception as e:
            print(e)
            logging.error("未知错误，错误信息：" + str(traceback.format_exc()))

        else:
            logging.info("登录'%s',期望'%s',成功" % ("defang1", "德芳理财"))



if __name__ == '__main__':
    unittest.main()