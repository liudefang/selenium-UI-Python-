# -*- encoding: utf-8 -*-
# @Time    : 2017/12/21 13:56
# @Author  : mike.liu
# @File    : test_demo5.py

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


        try:

            self.driver.find_element_by_xpath("//*[@name='username']").send_keys("defang2")
            self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
            self.driver.find_element_by_xpath("//*[@class='submit_wrap']").click()

            self.driver.find_element_by_xpath("//a[contains(.,'退出系统')]").click()
        except Exception as msg:
            print('msg:%s' % msg)




            #图片名称加了一个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            pic = self.driver.get_screenshot_as_file('D:\\pythonpj\\testfour\\exceptionpictures\\%s.png' % nowTime)
            print("截图结果:%s" %pic)
            print("nowTime:" + nowTime)

        time.sleep(5)

        #assert '德芳客服' in self.driver.page_source

        time.sleep(5)