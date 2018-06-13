# -*- encoding: utf-8 -*-
import unittest

import time
from selenium import webdriver
from selenium.webdriver import ActionChains


lcs_dic = {"username": "defang1", "password": "123", "exc_name": "德芳理财"}
yw_dic = {"username": "defang3", "password": "123", "exc_name": "德芳运维"}

class login_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''测试固件setUp的代码，主要用于测试的前期准备工作'''
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(8)
        cls.driver.get("http://10.1.2.88:8080/login.jsp")
    @classmethod
    def tearDownClass(cls):
        '''测试结束之后的清理，一般是关闭浏览器'''

        cls.driver.quit()

    def login_case(self, username, password, exc_name):
        '''这里一定要以test开头'''

        self.driver.find_element_by_xpath("//*[@name='username']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
        self.assertEqual(self.driver.title, '深圳市金斧子网络科技有限公司-ERP', msg='访问erp成功')
        time.sleep(5)

        assert exc_name in self.driver.page_source
        time.sleep(5)
        # 先让选项框弹出来
        mouse = self.driver.find_element_by_xpath("//*[@id='app']/div/div/section/header/section/div[2]/div[4]/div/div/div[1]/span[1]")
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 再点击选项框里面的元素
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[text()='退出系统']").click()

        time.sleep(5)

        print("标题:" + self.driver.title)

        time.sleep(5)

    def test_login_01(self):
        '''理财师登录'''
        self.login_case(lcs_dic["username"], lcs_dic["password"], lcs_dic["exc_name"])
    #
    # def test_login_02(self):
    #     '''项目运维登录'''
    #     self.login_case(yw_dic["username"], yw_dic["password"], yw_dic["exc_name"])




if __name__ == '__main__':
    unittest.main()









