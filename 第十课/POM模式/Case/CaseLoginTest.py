# -*- encoding: utf-8 -*-
# @Time    : 2018/7/5 19:52
# @Author  : mike.liu
# @File    : CaseLoginTest.py
import traceback
import unittest

from Util.Log import *
from Base.BasePage import *
from Page.LoginPage import *
from Util.browser_engine import *


class CaseLoginTest(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def test_login1(self):

        loginpage = LoginPage(self.driver)
        try:
            # 找到用户名和密码输入框，并输入测试数据
            loginpage.userNameObj("defang1")
            loginpage.passwordObj("123")

            # 找到登录按钮，并单击
            loginpage.loginButton()
            loginpage.sleep(3)
            # 断言期望结果是否出现在页面源代码中
            loginpage.assert_string_in_pagesource("德芳理财")
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

    def tearDown(self):

        loginpage = LoginPage(self.driver)
        loginpage.close_browser()

if __name__ == '__main__':
    unittest.main()