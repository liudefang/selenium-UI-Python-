# -*- encoding: utf-8 -*-
# @Time    : 2018/8/30 17:56
# @Author  : mike.liu
# @File    : CustomerPage.py
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile


class CustomerPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.CustomerOptions = self.parseCF.getItemsSection("erp_Customer")

    # 进入到财富中心客户列表
    def fortuneCenter(self):
        try:
            # 从定位表达式配置文件中读取添加客户的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.fortuneCenter".lower()].split(">")
            # 获取添加客户资料页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 点击添加按钮
    def addLink(self):
        try:
            # 从定位表达式配置文件中读取添加客户的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.AddLink".lower()].split(">")
            # 获取添加客户资料页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 切换到添加客户资料的fram里面
    def fram(self):
        try:
            # 从定位表达式配置文件中读取fram的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.frame".lower()].split(">")
            # 获取添加客户资料页面的fram，并返回给调用者
            self.driver.switch_to.frame(locatorExpression)
        except Exception as e:
            raise e

    # 选择记录类型
    def recordType(self):
        try:
            # 从定位表达式配置文件中读取记录类型的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.recordType".lower()].split(">")
            # 获取添加客户资料页面的选择记录类型对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 输入客户姓名
    def userName(self):
        try:
            # 从定位表达式配置文件中读取客户姓名的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.username".lower()].split(">")
            # 获取添加客户资料页面的客户姓名类型对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 选择获取方式
    def fromType(self):
        try:
            # 从定位表达式配置文件中读取获取方式的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.fromType".lower()].split(">")
            # 获取添加客户资料页面的获取方式对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 选择性别
    def sex(self):
        try:
            # 从定位表达式配置文件中读取性别的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.sex".lower()].split(">")
            # 获取添加客户资料页面的性别对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 选择预约类型
    def ctype(self):
        try:
            # 从定位表达式配置文件中读取预约类型的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.ctype".lower()].split(">")
            # 获取添加客户资料页面的预约类型对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 输入手机号码
    def phoneNumber(self):
        try:
            # 从定位表达式配置文件中读取手机号码的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.phoneNumber".lower()].split(">")
            # 获取添加客户资料页面的手机号码对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 选择预约时间
    def yytime(self):
        try:
            # 从定位表达式配置文件中读取预约时间的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.yytime".lower()].split(">")
            # 获取添加客户资料页面的预约时间对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def ifram(self):
        try:
            # 从定位表达式配置文件中读取预约时间的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.iframe".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            # return elementObj
            self.driver.switch_to.frame(elementObj)
        except Exception as e:
            raise e

    # 选择预约时间为今天
    def dpTodayInput(self):
        try:
            # 从定位表达式配置文件中读取预约时间的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.dpTodayInput".lower()].split(">")
            # 获取添加客户资料页面的预约时间对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 切换出ifram
    def tofram(self):
        try:
            # 切换出当前的fram
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    # 点击保存按钮
    def saveCustomer(self):
        try:
            # 从定位表达式配置文件中读取保存按钮的定位表达式
            locateType, locatorExpression = self.CustomerOptions["CustomerPage.saveCustomer".lower()].split(">")
            # 获取添加客户资料页面的保存对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
