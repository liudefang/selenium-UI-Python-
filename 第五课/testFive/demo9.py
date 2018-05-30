# -*- encoding: utf-8 -*-
# @Time    : 2017/12/28 11:37
# @Author  : mike.liu
# @File    : demo9.py
import logging

import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("https://beta-erp.jfz.com/login.jsp")
title = driver.title
#if (title == "深圳市金斧子网络科技有限公司-ERP"):
#    print("测试成功，结果和预期结果匹配！")
driver.find_element_by_xpath("//*[@name='username']").send_keys("mike.liu")
driver.find_element_by_xpath("//*[@name='password']").send_keys("erp@123")
driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
#print("标题"+ driver.title)
logging.info("标题"+ driver.title)
time.sleep(5)

#driver.find_element_by_xpath("//*[@id='10000013510557']").click()

time.sleep(5)
# 先让选项框弹出来
mouse = driver.find_element_by_xpath("//*[@id='app']/div/div/section/header/section/div[2]/div[2]/div/span")
ActionChains(driver).move_to_element(mouse).perform()
# 再点击选项框里面的元素
time.sleep(3)
driver.find_element_by_xpath("//*[text()='客服系统']").click()
