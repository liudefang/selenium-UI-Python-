# -*- encoding: utf-8 -*-
# @Time    : 2018/12/6 18:07
# @Author  : mike.liu
# @File    : PageAction.py
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from 第十三课.KeyWorkFrameWorkDemo.config.VarConfig import *
from 第十三课.KeyWorkFrameWorkDemo.util.DirAndTime import getCurrentTime, createCurrentDateDir
from 第十三课.KeyWorkFrameWorkDemo.util.ObjectMap import getElement

driver = None
# 全局的等待类实例对象
waitUtil = None
def open_browser(browserName, *args):
    # 打开浏览器
    global driver, waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path=ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            # 创建Chrome浏览器的一个options实例对象
            chrome_options = Options()
            # 添加屏蔽--ignore-certificate-errors提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignore-certificate-errors"])
            driver = webdriver.Chrome(
                executable_path=chromeDriverFilePath,
                chrome_options=chrome_options)
        else:
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
        # driver对象创建成果后，创建等待类实例对象
        waitUtil = waitUtil(driver)
    except Exception as e:
        raise e

def visit_url(url, *args):
    # 访问某个网址
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*args):
    # 关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def sleep(sleepSeconds, *args):
    # 强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e
def clear(locationType, locatorExpression, *args):
    # 清除输入框内容
    global driver
    try:
        getElement(driver, locationType, locatorExpression).clear()
    except BaseException as e:
        raise e
def input_string(locationType, locatorExpression, inputContent):
    # 在页面输入框输入数据
    global driver
    try:
        getElement(driver, locationType, locatorExpression).send_keys(inputContent)
    except BaseException as e:
        raise e

def click(locationType, locatorExpression, *args):
    # 单击页面元素
    global driver
    try:
        getElement(driver, locationType, locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString, *args):
    # 断言页面源码是否存在关键字或关键字字符串
    global driver
    try:
        assert assertString in driver.page_source, "%s not found in page source!" % assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def getTitle(*args):
    # 获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e


def getPageSoure(*args):
    # 获取页面源码
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

def switch_to_frame(locationType, frameLocationExpression, *args):
    # 切换进入frame
    global driver
    try:
        driver.switch_to_frame(driver, locationType, frameLocationExpression).click()
    except Exception as e:
        raise e
def switch_to_default_content(*args):
    # 切出fram
    global driver
    try:
        driver.switch_to_default_content()
    except Exception as e:
        raise e
def current_window_handle(*args):
    # 切换到新打开的页面
    global driver
    try:
           driver.switch_to.window(driver.window_handles[1])
           print("新窗口标题:", driver.title)
    except Exception as e:
        raise e


def maximize_browser():
    # 窗口最大化
    global driver
    try:
        driver.maximmize_window()
    except Exception as e:
        raise e


def capture_screen(*args):
    # 获取屏幕图片
    global driver
    curtTime = getCurrentTime()
    picNmaeAndPath = str(createCurrentDateDir()) + "\\" + str(curtTime) + ".png"
    try:
        driver.get_screenshot_as_file(picNmaeAndPath.replace('\\', r'\\'))
    except Exception as e:
        raise e
    else:
        return picNmaeAndPath

def wait_Presence_Of_Element_Located(locationType, locatorExpression, *args):
    '''显式等待页面元素出现在dom中，但并不一定可见,则返回改页面元素对象'''
    global driver
    try:
        waitUtil.presence_Of_Element_Located(locationType, locatorExpression, *args)
    except Exception as e:
        raise e
def wait_Frame_To_Be_Available_And_Switch_To_It(locationType, locatorExpression, *args):
    '''检查frame是否存在，存在则切换进frame控件中'''
    global waitUtil
    try:
        waitUtil.Frame_To_Be_Available_And_Switch_To_It(locationType, locatorExpression, *args)
    except Exception as e:
        raise e
def waitVisibilityOfElementLocated(locationTpye, locatorExpression, *args):
    '''显式等待页面元素出现dom中，并且可见，存在返回改页面元素对象'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationTpye, locatorExpression, *args)
    except Exception as e:
        raise e
