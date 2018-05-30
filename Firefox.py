#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2017/10/13 10:57
 
@author: 'mike.liu' 
'''

'''from selenium import webdriver #导入WebDriver包
driver = webdriver.Firefox()   #初始化一个火狐浏览器实例：driver
driver.maximize_window()   #最大化浏览器
driver.get("http://10.1.2.58:8080/login.jsp")  # 通过get()方法，打开一个url站点

driver.quit()'''

from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Ie()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://10.1.2.58:8080/login.jsp")

