#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2018/1/18 9:50
 
@author: 'mike.liu' 
'''
import unittest

from selenium import webdriver


class BrowserTest(unittest.TestCase):

    def setUp(self):
        '''测试固件setUp的代码，主要用于测试的前期准备工作'''
        self.driver = webdriver.Chrome()
        print('谷歌浏览器启动')
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

        self.driver.get("https://qa1-erp.jfz.com")

    def tearDown(self):
        '''测试结束之后的清理，一般是关闭浏览器'''

        self.driver.quit()



    def test_firefox(self):
        '''这里一定要以test开头'''

        self.driver.find_element_by_xpath("//*[@name='username']").send_keys("defang2")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
        self.driver.find_element_by_xpath("//*[@class='submit_wrap']").click()

