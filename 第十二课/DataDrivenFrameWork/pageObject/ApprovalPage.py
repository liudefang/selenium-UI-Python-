# -*- encoding: utf-8 -*-
# @Time    : 2018/8/28 20:02
# @Author  : mike.liu
# @File    : ApprovalPage.py
from util.ObjectMap import getElement
from util.ParseConfigurationFile import ParseConfigFile


class ApprovalPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.ApprovalOptions = self.parseCF.getItemsSection("erp_ApprovalPage")

    # 切换到审批流的ifram里面
    def fram(self):
        try:
            # 从定位表达式配置文件中读取fram的定位表达式
            locateType, locatorExpression = self.ApprovalOptions["ApprovalPage.frame".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 点击审批流的链接
    def approvalBut(self):
        try:
            # 从定位表达式配置文件中读取审批链接的定位表达式
            locateType, locatorExpression = self.ApprovalOptions["ApprovalPage.click_Approval".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

        # 切换到新的窗口
    def current_window_handle(self):
        try:
            new_window = self.driver.window_handles[1]
            self.driver.switch_to.window(new_window)
            return 'Pass', '切换到新窗口成功'
        except Exception as e:
            raise e
            return 'Fail', '切换到新窗口失败'

    # 点击审批流的同意按钮
    def approvalbtnAgree(self):
        try:
            # 从定位表达式配置文件中读取审批链接的定位表达式
            locateType, locatorExpression = self.ApprovalOptions["ApprovalPage.click_btnAgree".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 切换入同意的弹框的ifram
    def xpathfram(self):
        try:
            # 从定位表达式配置文件中读取fram的定位表达式
            locateType, locatorExpression = self.ApprovalOptions["ApprovalPage.btnAgree_frame".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 点击填写意见的确定按钮
    def approvaldataFormSave(self):
        try:
            # 从定位表达式配置文件中读取审批链接的定位表达式
            locateType, locatorExpression = self.ApprovalOptions["ApprovalPage.click_dataFormSave".lower()].split(">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

        # 断言文本内的提示信息中是否存在某关键字或关键字字符串
    def assertText(self):
        try:
            aElement = self.driver.find_element_by_class_name("l-dialog-content")
            a_text = aElement.text
            # print("a_text:"+a_text)
            assert "执行任务成功!" in a_text
        except AssertionError as e:
            raise e

    # 点击同意的确定按钮
    def approvalbtnDialog(self):
        try:
            # 从定位表达式配置文件中读取审批链接的定位表达式
            locateType, locatorExpression = self.ApprovalOptions["ApprovalPage.click_btnDialog".lower()].split(
                ">")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e