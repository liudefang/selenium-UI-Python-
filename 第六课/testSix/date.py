# -*- encoding: utf-8 -*-
# @Time    : 2018/1/10 19:30
# @Author  : mike.liu
# @File    : date.py
import logging

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
driver.find_element_by_xpath("//*[@id='10000013510266']").click()
assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
#print("标题"+ driver.title)
logging.info("标题"+ driver.title)
time.sleep(5)
assert "德芳运维" in driver.page_source
time.sleep(5)
#点击私募菜单
driver.find_element_by_xpath("//*[@name='私募产品']").click()
time.sleep(5)
#进入到ifram
#driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'iframe')]"))
driver.switch_to.frame("iframe10000013510309")
#进行搜索
driver.find_element_by_xpath("//*[@name='Q_crmCode_SL']").send_keys("D20171228001")

#点击查找按钮
driver.find_element_by_xpath("//*[@id='btnSearch']").click()
time.sleep(5)
#点击明细按钮
driver.find_element_by_xpath("//*[text()='明细']" ) .click()



#点击添加费率按钮

driver.find_element_by_xpath("//*[@id='addFee']").click()
time.sleep(5)
#输入协议主体机构
driver.find_element_by_xpath("//*[@id='agreementOrgId']").send_keys( "夏道山测试数据" )

#选择协议类型
agreementType =driver.find_element_by_xpath("//*[@id='agreementType']")
agreementType.find_element_by_xpath("//option[@value='1']").click()
#输入协议有效时间
driver.find_element_by_xpath("//*[@id='validityFrom']").send_keys( "2018-01-12")

driver.find_element_by_xpath("//*[@id='validityTo']").send_keys( "2018-01-20")

