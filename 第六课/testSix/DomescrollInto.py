#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2018/1/18 11:41
 
@author: 'mike.liu' 
'''

import logging
import os
import time


from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("http://10.1.2.211:8080/login.jsp")
title = driver.title
#if (title == "深圳市金斧子网络科技有限公司-ERP"):
#    print("测试成功，结果和预期结果匹配！")
driver.find_element_by_xpath("//*[@name='username']").send_keys("defang3")
driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
driver.find_element_by_xpath("//*[@class='submit_wrap']").click()

assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
#print("标题"+ driver.title)
logging.info("标题"+ driver.title)
time.sleep(5)
assert "德芳运维" in driver.page_source
time.sleep(5)


driver.find_element_by_xpath("//*[@name='私募产品']").click()

time.sleep(5)

driver.switch_to.frame("iframe10000013510309")
time.sleep(3)

driver.find_element_by_xpath("//*[@name='Q_crmCode_SL']").send_keys("D20171228001")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='btnSearch']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[text()='明细']").click()
time.sleep(3)
#进行滚动，滚动到最下方进行操作
#driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")

#使用JavaScript的scrollIntoView函数将被遮挡的元素滚动到可见屏幕
#scrollIntoView(true)表示将元素滚动屏幕中间
driver.execute_script("document.getElementById('editOpenDay').scrollIntoView(true);")
#使用JavaScript的scrollby方法，使用0和800横纵坐标参数
#driver.execute_script("window.scrollBy(0,800);")