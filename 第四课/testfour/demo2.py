# -*- encoding: utf-8 -*-
# @Time    : 2017/12/20 19:30
# @Author  : mike.liu
# @File    : demo2.py

import unittest
import time
from selenium import webdriver

class testfour(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''测试固件setUp的代码，主要用于测试的前期准备工作'''
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(8)
        cls.driver.get("https://qa-erp.jfz.com")

    @classmethod
    def tearDownClass(cls):
        '''测试结束之后的清理，一般是关闭浏览器'''

        cls.driver.quit()

    def test_login01(self):
        '''这里一定要以test开头'''

        self.driver.find_element_by_xpath("//*[@name='username']").send_keys("defang2")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
        self.driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
        self.driver.find_element_by_xpath("//*[@id='10000012200328']/a").click()
        self.assertEqual(self.driver.title,'深圳市金斧子网络科技有限公司-ERP',msg='访问erp失败')
        time.sleep(5)

        assert '客服系统' in self.driver.page_source
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains(.,'退出系统')]").click()
        time.sleep(5)

        print("标题:"+ self.driver.title)


        time.sleep(5)

    def test_login02(self):
        '''这里一定要以test开头'''

        self.driver.find_element_by_xpath("//*[@name='username']").send_keys("defang3")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
        self.driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
        self.driver.find_element_by_xpath("//*[@id='10000012200329']/a").click()
        self.assertEqual(self.driver.title, '深圳市金斧子网络科技有限公司-ERP', msg='访问erp失败')
        time.sleep(5)
        assert '德芳运维' in self.driver.page_source
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains(.,'退出系统')]")
        time.sleep(5)

        print("标题:" + self.driver.title)


        time.sleep(5)

if __name__ == '__main__':
    unittest.main()