# -*- encoding: utf-8 -*-
# @Time    : 2018/7/5 19:30
# @Author  : mike.liu
# @File    : login.py

import logging
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("http://10.1.2.58:8080/login.jsp")
title = driver.title
driver.find_element_by_xpath("//*[@name='username']").send_keys("defang2")
driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
driver.find_element_by_xpath("//*[@id='10000012200328']/a").click()
assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
logging.info("标题"+ driver.title)
time.sleep(5)
assert "德芳客服" in driver.page_source
time.sleep(5)
print(driver.title)