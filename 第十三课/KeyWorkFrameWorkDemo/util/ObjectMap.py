# -*- encoding: utf-8 -*-
# @Time    : 2018/12/6 17:38
# @Author  : mike.liu
# @File    : ObjectMap.py

from selenium.webdriver.support.wait import WebDriverWait


def getElement(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locateType, value=locatorExpression))
        return element
    except Exception as e:
        raise e


# 获取多个相同页面元素对象，以list返回
def getElements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x: x.find_elements(by=locateType,value=locatorExpression))
        return elements
    except Exception as e:
        raise e