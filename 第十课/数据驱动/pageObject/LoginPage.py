# -*- encoding: utf-8 -*-
# @Time    : 2018/7/5 19:51
# @Author  : mike.liu
# @File    : LoginPage.py

from Util.ObjectMap import *


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def userNameObj(self):
        try:
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, "xpath", '//*[@name="username"]')
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//*[@name='password']")
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, "xpath", "//*[@class='submit_wrap']")
            return elementObj
        except Exception as e:
            raise e
