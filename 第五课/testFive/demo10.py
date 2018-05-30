# -*- encoding: utf-8 -*-
# @Time    : 2017/12/28 14:05
# @Author  : mike.liu
# @File    : demo10.py


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.get("https://www.baidu.com")
time.sleep(3)
# 先让选项框弹出来
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
# 再点击选项框里面的元素
driver.find_element_by_link_text("搜索设置").click()
