# -*- encoding: utf-8 -*-
# @Time    : 2017/12/20 9:14
# @Author  : mike.liu
# @File    : testfour.py
import unittest
import time
from selenium import webdriver

class testfour(unittest.TestCase):

    def setUp(self):
        '''测试固件setUp的代码，主要用于测试的前期准备工作'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://qa1-erp.jfz.com")

    def tearDown(self):
        '''测试结束之后的清理，一般是关闭浏览器'''

        self.driver.quit()

    def test_login(self):
        '''这里一定要以test开头'''

        self.driver.find_element_by_xpath("//*[@name='username']").send_keys("defang2")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
        self.driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
        self.assertEqual(self.driver.title,'深圳市金斧子网络科技有限公司-ERP',msg='访问erp失败')

        print("标题"+ self.driver.title)

        time.sleep(5)
        assert '德芳客服' in  self.driver.page_source
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()