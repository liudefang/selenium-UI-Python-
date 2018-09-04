# -*- encoding: utf-8 -*-
# @Time    : 2018/8/30 15:33
# @Author  : mike.liu
# @File    : ApprovalAction.py
from 第十二课.DataDrivenFrameWork.pageObject.ApprovalPage import ApprovalPage


class ApprovalAction(object):
    def __init__(self):
        print("审批流页面")

    @staticmethod
    def approval(driver):
        try:
            # 创建审批流的页面实例对象
            ap = ApprovalPage(driver)
            # 进入到fram框，以便点击
            ap.fram()
            # 点击审批流的链接
            ap.approvalBut().click()
            #  切换到新的窗口
            ap.current_window_handle()
            # 点击审批流的同意按钮
            ap.approvalbtnAgree().click()
            # 切换入同意的弹框的ifram
            ap.xpathfram()
            # 点击填写意见的确定按钮
            ap.approvaldataFormSave().click()
            # 断言文本内的提示信息中是否存在某关键字或关键字字符串
            ap.assertText()
            # 点击同意的确定按钮
            ap.approvalbtnDialog().click()
        except Exception as e:
            raise e

