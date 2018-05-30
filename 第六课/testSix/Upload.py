#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2018/1/15 16:34
 
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
driver.find_element_by_xpath("//*[text()='查看']").click()
time.sleep(5)






#  得到当前窗口的句柄
now_handle = driver.current_window_handle
print("当前窗口句柄："+now_handle)
# 得到所有窗口的句柄
all_handles = list(driver.window_handles)
print(all_handles)
print("++++",driver.window_handles[1])
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

print(driver.title)
#直接send_keys方式上传文件
#driver.find_element_by_xpath("//input[@name='file']").send_keys("D:\图片\协议主体.jpg")
time.sleep(5)
#通过第三方工具进行上传
driver.find_element_by_tag_name("label").click()
os.system("D:\\workspace\\Erp-Automated-Test\\upload.exe"+ " " + "chrome" + " " + "D:\\图片\\合同签字页.jpg") # 你自己本地的这个.exe文件绝对路径


assert "下载" in driver.page_source
time.sleep(10)
driver.close()
