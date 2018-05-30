# -*- encoding: utf-8 -*-
# @Time    : 2017/12/27 19:26
# @Author  : mike.liu
# @File    : demo7.py

import logging
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("http://10.1.2.58:8080/login.jsp")
title = driver.title
#if (title == "深圳市金斧子网络科技有限公司-ERP"):
#    print("测试成功，结果和预期结果匹配！")
driver.find_element_by_xpath("//*[@name='username']").send_keys("defang2")
driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
driver.find_element_by_xpath("//*[@id='10000012200328']/a").click()
assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
#print("标题"+ driver.title)
logging.info("标题"+ driver.title)
time.sleep(5)
assert "德芳客服" in driver.page_source
time.sleep(5)
#driver.switch_to.frame("iframe89892232323")
driver.switch_to.frame(0)
driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[1]/ul/li[1]/div[1]").click()

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