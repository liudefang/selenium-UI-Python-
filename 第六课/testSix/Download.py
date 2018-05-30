# -*- encoding: utf-8 -*-
# @Time    : 2018/1/13 15:14
# @Author  : mike.liu
# @File    : Download.py

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
# 设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。
profile = webdriver.FirefoxProfile()
# 设置成0表示下载到桌面;设置成1表示下载到默认路径;设置成2则可以保存到指定目录;
profile.set_preference('browser.download.folderList', 2)
# 指定下载文件到你想放的路径
profile.set_preference('browser.download.dir', 'd:\\downloadFiles')
# 开始下载时候显示是否显示进度框 (这个设置目前没生效)
profile.set_preference("browser.download.manager.showWhenStarting", False)
# 对所给出文件类型不再弹出框进行询问
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
driver = webdriver.Firefox(firefox_profile=profile)
# 打开有道云笔记
driver.get("http://note.youdao.com/")
# 点立即下载按钮
driver.find_element_by_id("download-btn").click()

