# -*- encoding: utf-8 -*-
# @Time    : 2018/8/9 19:29
# @Author  : mike.liu
# @File    : LoginAction.py

import time
from selenium import webdriver
from pageObject.LoginPage import LoginPage
class LoginAction(object):
    def __init__(self):
        print("登录....")
    @staticmethod
    def login(driver, username, password):
        try:
            login = LoginPage(driver)
            # 输入登录用户名
            login.userNameObj().send_keys(username)
            # 输入登录密码
            login.passwordObj().send_keys(password)
            # 点击登录按钮
            login.loginButton().click()
        except Exception as e:
            raise e
