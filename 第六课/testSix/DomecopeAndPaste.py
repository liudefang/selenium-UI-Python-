#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2018/1/18 14:10
 
@author: 'mike.liu' 
'''
import logging

import time
from selenium import webdriver
import win32con
import win32clipboard as w

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

#设置剪贴板
# 读取粘贴板

def getText():
    # 打开剪贴板
    w.OpenClipboard()
    # 获取剪贴板中的数据
    d = w.GetClipboardData(win32con.CF_TEXT)
    # 关闭剪贴板
    w.CloseClipboard()
    # 返回剪贴板数据个调用者
    return d


# 设置剪贴板内容

def setText(aString):
    # 打开剪贴板
    w.OpenClipboard()
    # 清空剪贴板
    w.EmptyClipboard()
    # 将数据astring写入剪贴板
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    # 关闭剪贴板
    w.CloseClipboard()


driver.get("http://10.1.2.211:8080/login.jsp")
title = driver.title
#if (title == "深圳市金斧子网络科技有限公司-ERP"):
#    print("测试成功，结果和预期结果匹配！")
#定义即将要设置到剪贴板中的内容
content= 'defang3'
#将content变量中的内容设置到剪贴板中
setText(content)
#从剪贴板中获取刚设置到剪贴板中的内容
getContent = getText()
print(getContent.decode("gbk").encode("utf-8"))
#将焦点切换到用户名输入框中
driver.find_element_by_xpath("//*[@name='username']").click()

#模拟ctrl+v组合键，将从剪贴板中获取到的内容粘贴到用户名输入框中
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

#driver.find_element_by_xpath("//*[@name='username']").send_keys("defang3")
driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
driver.find_element_by_xpath("//*[@id='10000013510266']").click()
assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
#print("标题"+ driver.title)
logging.info("标题"+ driver.title)
time.sleep(5)
assert "德芳运维" in driver.page_source