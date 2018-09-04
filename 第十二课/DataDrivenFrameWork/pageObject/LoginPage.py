# -*- encoding: utf-8 -*-
# @Time    : 2018/8/2 14:04
# @Author  : mike.liu
# @File    : LoginPage.py
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemsSection("erp_login")
        # print(self.loginOptions)

    def userNameObj(self):
        try:
            # 从定位表达式配置文件中读取fram的定位表达式
            locateType, locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e