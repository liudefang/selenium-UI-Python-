# -*- encoding: utf-8 -*-
# @Time    : 2018/12/6 17:58
# @Author  : mike.liu
# @File    : TestErpApprovalflow.py
import time

from selenium import webdriver

from 第十三课.KeyWorkFrameWorkDemo.action.PageAction import *
from 第十三课.KeyWorkFrameWorkDemo.util.ObjectMap import getElement
from 第十三课.KeyWorkFrameWorkDemo.util.WaitUtil import WaitUtil

# / *用于编写具体的测试操作代码 * /


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


if __name__ == '__main__':
    TestErpApprovalflow()





