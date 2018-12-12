# -*- encoding: utf-8 -*-
# @Time    : 2018/11/21 9:37
# @Author  : mike.liu
# @File    : WaitUtil.py
import logging
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class WaitUtil(object):

    def __init__(self, driver):
        self.locationTypeDict = {
             "xpath": By.XPATH,
             "id": By.ID,
             "name": By.NAME,
             "css_selector": By.CSS_SELECTOR,
             "class_name": By.CLASS_NAME,
             "tag_name": By.TAG_NAME,
             "link_text": By.LINK_TEXT,
             "partial_link_text": By.PARTIAL_LINK_TEXT
         }
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def presence_Of_Element_Located(self, locatorMethod, locatorExpression, *arg):
        ''''显式等待页面元素出现在DOM中，但并不一定课件，存在则返回该页面元素对象'''
        try:
            if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(EC.presence_of_all_elements_located((
                    self.locationTypeDict[locatorMethod.lower()], locatorExpression)))
            else:
                raise TypeError("未找到定位方式，请确认定位方式是否写正确")
        except Exception as e:
            raise e

    def frame_available_and_swith_to_it(self, locationType, locatorExpression, *arg):
        '''检查fram是否存在，存在则切换金frame控件中'''
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it
                            ((self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception as e:
            raise e
    # 抛出异常信息给上层调用者

    def visibility_element_located(self, locationType, locatorExpression):
        '''显示等待页面元素的出现'''
        try:
            element = self.wait.until(EC.visibility_of_element_located
                                      ((self.locationTypeDict[locationType.lower()], locatorExpression)))
            return element
        except Exception as e:
            raise e


if __name__ == "__main__":
    # 单元测试
    driver = webdriver.Chrome()
    driver.maximize_window()  # 最大化浏览器
    driver.implicitly_wait(8)  # 设置隐式时间等待

    driver.get("http://10.1.2.58:8080/login.jsp")
    title = driver.title
    # if (title == "深圳市金斧子网络科技有限公司-ERP"):
    #    print("测试成功，结果和预期结果匹配！")
    driver.find_element_by_xpath("//*[@name='username']").send_keys("defang3")
    driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
    driver.find_element_by_xpath("//*[@class='login-btn']").click()

    assert "深圳市金斧子网络科技有限公司-ERP" in driver.title
    # print("标题"+ driver.title)
    logging.info("标题" + driver.title)
    time.sleep(5)
    assert "德芳运维" in driver.page_source
    time.sleep(5)

    driver.find_element_by_xpath("//*[@name='私募证券']").click()

    time.sleep(5)
    waitUtil = WaitUtil(driver)
    waitUtil.frame_available_and_swith_to_it("id", "iframe10000013510309")
    time.sleep(3)

    e = waitUtil.visibility_element_located("xpath", "//*[@name='Q_crmCode_SL']")
    e.send_keys("D20171228001")
    # driver.find_element_by_xpath("//*[@name='Q_crmCode_SL']").send_keys("D20171228001")
    time.sleep(3)
    el = waitUtil.visibility_element_located("xpath", "//*[@id='btnSearch']")
    el.click()
    time.sleep(5)
    driver.quit()