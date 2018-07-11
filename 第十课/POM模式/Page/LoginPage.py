# -*- encoding: utf-8 -*-
# @Time    : 2018/7/5 19:51
# @Author  : mike.liu
# @File    : LoginPage.py
from Base.BasePage import Action


class LoginPage(Action):

    user_name = "xpath=>//*[@name='username']"
    pass_word = "xpath=>//*[@name='password']"
    login_Button = "xpath=>//*[@class='login-btn']"

    def userNameObj(self, inputContent):
        try:
            self.input_string(self.user_name, inputContent)
        except Exception as e:
            raise e

    def passwordObj(self, inputContent):
        try:
            self.input_string(self.pass_word, inputContent)
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            self.click(self.login_Button)
        except Exception as e:
            raise e
