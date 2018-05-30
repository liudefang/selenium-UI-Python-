#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2018/1/17 19:41
 
@author: 'mike.liu' 
'''


import logging
import os
import time


from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("http://10.1.2.88:8080/login.jsp")
title = driver.title
#if (title == "深圳市金斧子网络科技有限公司-ERP"):
#    print("测试成功，结果和预期结果匹配！")
driver.find_element_by_xpath("//*[@name='username']").send_keys("defang1")
driver.find_element_by_xpath("//*[@name='password']").send_keys("123456")
driver.find_element_by_xpath("//*[@class='submit_wrap']").click()

assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
#print("标题"+ driver.title)
logging.info("标题"+ driver.title)
time.sleep(5)
assert "德芳理财" in driver.page_source
time.sleep(5)

driver.find_element_by_xpath("//*[@id='70000000030487']").click()

driver.find_element_by_xpath("//*[@name='打款心得']").click()
time.sleep(3)
driver.switch_to.frame("iframe30000008531752")

#点击编辑按钮
driver.find_element_by_xpath("//*[text()='编辑']").click()
time.sleep(5)
driver.switch_to.frame("ueditor_0")
driver.find_element_by_tag_name("body").clear()
driver.find_element_by_tag_name("body").send_keys("测试打款心得-Python")
driver.switch_to.parent_frame()
time.sleep(5)
driver.find_element_by_class_name("l-dialog-btn-inner").click()