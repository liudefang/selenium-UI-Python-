# -*- encoding: utf-8 -*-
# @Time    : 2018/7/9 15:38
# @Author  : mike.liu
# @File    : browser_engine.py
import configparser

from Util.Log import *

import os.path
from selenium import webdriver

from config.VarConfig import *

driver = None


class BrowserEngine(object):
    chrome_driver_path = chromeDriverFilePath
    firfox_driver_path = firefoxDriverFilePath
    ie_driver_path = ieDriverFilePath

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()

        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("选择的浏览器是:%s" % browser)
        url = config.get("testServer", "URL")
        logger.info("测试的服务器地址是:%s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("firefox 浏览器已经启动")
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("Chrome 浏览器已经启动")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("IE 浏览器已经启动")

        driver.get(url)
        logger.info("打开的URL地址是:%s" % url)
        driver.maximize_window()
        logger.info("浏览器最大化")
        driver.implicitly_wait(10)
        logger.info("等待10秒")
        return driver

