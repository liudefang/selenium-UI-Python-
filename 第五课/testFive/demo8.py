# -*- encoding: utf-8 -*-
# @Time    : 2017/12/28 10:55
# @Author  : mike.liu
# @File    : demo8.py
import logging

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("https://beta-erp.jfz.com/login.jsp")
title = driver.title
#if (title == "深圳市金斧子网络科技有限公司-ERP"):
#    print("测试成功，结果和预期结果匹配！")
driver.find_element_by_xpath("//*[@name='username']").send_keys("mike1")
driver.find_element_by_xpath("//*[@name='password']").send_keys("erp@123")
driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
#print("标题"+ driver.title)
logging.info("标题"+ driver.title)
time.sleep(5)
#点击客户关系管理
driver.find_element_by_xpath("//*[@id='70000000030487']").click()
time.sleep(5)
#点击购买记录菜单
driver.find_element_by_xpath("//*[@name='购买记录']").click()

time.sleep(5)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'iframe10000003900200')]"))
# 直接通过xpath定位
time.sleep(5)
#driver.find_element_by_xpath("//*[@id='pageSize']/option[3]").click()

# 先定位下拉框
# s = driver.find_element_by_id("pageSize")
# s.find_element_by_xpath("//option[@value='15']").").click()
#二次定位
driver.find_element_by_id("pageSize").find_element_by_xpath("//option[@value='15']").click()


#driver.quit()