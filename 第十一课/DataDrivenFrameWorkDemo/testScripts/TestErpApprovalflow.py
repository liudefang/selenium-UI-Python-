# -*- encoding: utf-8 -*-
# @Time    : 2018/8/9 19:23
# @Author  : mike.liu
# @File    : TestErpApprovalflow.py

# 用于编写具体的测试操作代码 * /
from selenium import webdriver
import time
from appModules.LoginAction import LoginAction
def testErpLogin():
    try:
        # 启动谷歌浏览器
        driver = webdriver.Chrome(executable_path="E:\\Python36\\chromedriver")
        # 访问erp首页
        driver.get("https://qa1-erp.jfz.com")
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(5)
        # 登录erp
        LoginAction.login(driver, "defang1", "123")
        time.sleep(5)
        assert "德芳理财" in driver.page_source
    except Exception as e:
        raise e
    finally:
        # 退出浏览器
        driver.quit()



if __name__ == '__main__':
    # 进行单元测试
    testErpLogin()
    print("登录erp成功")



