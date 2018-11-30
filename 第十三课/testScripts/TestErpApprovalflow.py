# -*- encoding: utf-8 -*-
# @Time    : 2018/11/22 9:31
# @Author  : mike.liu
# @File    : TestErpApprovalflow.py

from 第十三课.action.PageAction import *


def TestErpApprovalflow():
    print("启动Chrome浏览器")
    open_browser("chrome")
    # 最大化浏览器窗口
    maximize_browser()
    print("访问erp登录页面")
    visit_url("http://10.1.2.58:8080/login.jsp")
    time.sleep(3)
    assert_string_in_pagesource("深圳市金斧子网络科技有限公司-ERP")
    print("输入登录用户名")
    input_string("xpath", "//*[@name='username']", "defang2")
    print("输入登录密码")
    # 输入密码
    input_string("xpath", "//*[@name='password']", "123")
    print("点击登录按钮")
    click("xpath", "//*[@class='login-btn']")
    time.sleep(5)
    assert_string_in_pagesource("德芳客服")
    time.sleep(5)
    wait_Frame_To_Be_Available_And_Switch_To_It("id", "iframe89892232323")
    print("点击审批流的链接")
    click("xpath", "html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[1]/ul/li[1]/div[1]")
    time.sleep(3)
    print("切换到新的窗口")

    current_window_handle()

    time.sleep(3)
    print("点击审批按钮")
    click("xpath", "//*[@id='btnAgree']")
    wait_Frame_To_Be_Available_And_Switch_To_It("xpath", "//iframe[contains(@id,'ligerwindow')]")
    time.sleep(3)
    print("点击填写意见的确定按钮")
    click("xpath", "//*[@id='dataFormSave']")
    time.sleep(5)
    print("点击同意的确定按钮")
    click("xpath", "//*[text()='确定']")
    print("关闭浏览器")
    close_browser()


if __name__ == '__main__':
    TestErpApprovalflow()