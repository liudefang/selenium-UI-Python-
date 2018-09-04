# -*- encoding: utf-8 -*-
# @Time    : 2018/9/3 11:44
# @Author  : mike.liu
# @File    : addcustomertest.py
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.maximize_window()  # 最大化浏览器
# driver.implicitly_wait(8)  # 设置隐式时间等待
#
# driver.get("http://10.1.2.211:8080/login.jsp")
# title = driver.title
# #if (title == "深圳市金斧子网络科技有限公司-ERP"):
# #    print("测试成功，结果和预期结果匹配！")
# driver.find_element_by_xpath("//*[@name='username']").send_keys("defang1")
# driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
# driver.find_element_by_xpath("//*[@class='login-btn']").click()
# time.sleep(5)
# driver.find_element_by_xpath("//*[@name='财富中心客户']").click()
# driver.switch_to.frame("iframe10000014545120")
# time.sleep(3)
# driver.find_element_by_xpath("//*[text()='添加']").click()
#
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='recordType']/option[@value='1']").click()
# driver.find_element_by_xpath("//*[@id='name']").send_keys("测试的")
# driver.find_element_by_xpath("//*[@id='fromType']/option[@value='6']").click()
# driver.find_element_by_xpath("//*[@id='sex']/option[@value='1']").click()
# driver.find_element_by_xpath("//*[@id='ctype']/option[@value='2']").click()
# driver.find_element_by_xpath("//*[@id='phoneNumber']").send_keys("10212345678")
# driver.find_element_by_xpath("//*[@id='yytime']").click()
#
# driver.switch_to.default_content()
# time.sleep(5)
# iframe = driver.find_element_by_xpath("/html/body/div[3]/iframe")
# driver.switch_to.frame(iframe)
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='dpTodayInput']").click()
# driver.switch_to.default_content()
# driver.switch_to.frame("iframe10000014545120")
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='saveCustomer']").click()

for i in range(2,4): # 根据因子迭代
    if i%2 == 0:      # 确定第一个因子
        print("能被2整除", i)
        # continue
    else:                  # 循环的 else 部分
        print("不能被2整除", i) # '是一个质数'

