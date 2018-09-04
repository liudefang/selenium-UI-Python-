# -*- encoding: utf-8 -*-
# @Time    : 2018/8/31 14:01
# @Author  : mike.liu
# @File    : TestAddCustomer.py

import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from appModules.LoginAction import LoginAction
from 第十二课.DataDrivenFrameWork.appModules.AddCustomerAction import AddCustomer
from 第十二课.DataDrivenFrameWork.config.VarConfig import *
from util.Log import *
from 第十二课.DataDrivenFrameWork.util.ParseExcel import ParseExcel

# 创建解析excel对象
excelObj = ParseExcel()
# 将excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)


def LaunchBrowser():
    # 创建Chrome浏览器的一个Options实例对象
    chrome_options = Options()
    # 向Options实例中添加禁用扩展插件的设置参数项
    chrome_options.add_experimental_option("excludeSwitches", ["--disable-extensions"])
    # 添加浏览器最大化的设置参数项，已启动就是最大化
    chrome_options.add_argument('--start-maximized')
    # 启动带有自定义设置的chrome浏览器
    driver = webdriver.Chrome(executable_path="E:\\Python36\\chromedriver", chrome_options=chrome_options)
    # 访问erp首页
    driver.get("https://qa1-erp.jfz.com")
    time.sleep(3)
    return driver


def TestAddCustomer():
    try:
        # 根据excel文件中sheet名称获取此sheet对象
        userSheet = excelObj.getSheetByName("登录账号")
        # 获取登录账号sheet中是否执行行列
        isExecuteUser = excelObj.getColumn(userSheet, account_isExecute)
        # 获取登录账号在sheet中的数据表列
        dataBookColumn = excelObj.getColumn(userSheet, account_dataBook)
        logging.info("测试理财师添加客户信息执行开始")
        for idx, i in enumerate(isExecuteUser[1:]):
            # 循环遍历登录账号的登录名，为需要执行的账号添加客户信息
            if i.value == "y":  # 表示要执行
                # 获取第i行的数据
                userRow = excelObj.getRow(userSheet, idx + 2)
                # 获取第i行中的用户名
                username = userRow[account_username - 1].value

                # 获取第i行中的密码
                password = str(userRow[account_password - 1].value)

                # logging.info(username, password)

                # 创建浏览器实例对象
                driver = LaunchBrowser()

                # 登录erp系统
                LoginAction.login(driver, username, password)
                # 登录3秒，让浏览器启动完成，以便正常进行后续操作
                time.sleep(3)
                # 获取为第i行中用户添加的客户信息数据表sheet名
                dataBookName = dataBookColumn[idx + 1].value
                # 获取对应的数据表对象
                dataSheet = excelObj.getSheetByName(dataBookName)
                # 获取了客户数据表中是否执行行列对象
                isExecuteData = excelObj.getColumn(dataSheet, customer_isExecute)
                contactNum = 0  # 记录添加成功客户的个数
                isExecuteNum = 0  # 记录需要执行客户的个数
                for id, data in enumerate(isExecuteData[1:]):
                    # 循环遍历是否执行添加客户列
                    # 如果被设置为添加，则进行客户添加操作
                    if data.value == "y":
                        # 如果第id行的客户被设置为执行，则isExecuteNum自增
                        isExecuteNum += 1
                        # 获取客户表第id+2行对象
                        rowContent = excelObj.getRow(dataSheet, id + 2)
                        # 获取客户姓名
                        customerUserName = rowContent[customer_customerUserName - 1].value

                        # 获取联系人手机号
                        customerPhoneNumber = rowContent[customer_customerPhoneNumber - 1].value
                        # 添加客户信息成功之后，获取断言信息
                        assertKeyWord = rowContent[customer_contactKeyWords - 1].value
                        # logging.info(customerUserName, customerPhoneNumber, assertKeyWord)

                        # 执行新建客户操作
                        AddCustomer.customer(driver, customerUserName, customerPhoneNumber)
                        time.sleep(2)
                        logging.info("添加客户 %s 成功" % customerPhoneNumber)
                        # 在添加客户工作表中写入添加客户执行时间
                        excelObj.writeCurrentTime(dataSheet, rowNo=id + 2, colsNo=customer_runTime)
                        try:
                            # 断言给定的关键字是否出现在页面中
                            assert assertKeyWord in driver.page_source
                        except AssertionError as e:
                            # 断言失败，在添加客户工作表中写入添加客户信息测试失败信息
                            excelObj.writeCell(dataSheet, "Faild", rowNo=id + 2, colsNo=customer_testResult, style="red")
                            logging.info("断言关键字 %s 失败" % assertKeyWord)
                        else:
                            # 断言成功，写入添加客户信息成功信息
                            excelObj.writeCell(dataSheet, "Pass", rowNo=id + 2, colsNo=customer_testResult,
                                               style="green")
                            contactNum += 1
                            logging.info("断言关键字 %s 成功" % assertKeyWord)
                    else:
                        ignorecustomerUserName = excelObj.getCellOfValue(dataSheet, rowNo=id + 2, colsNo=customer_customerUserName)
                        logging.info("客户 %s 被忽略执行" % ignorecustomerUserName)
                logging.info("contactNum = %s,isExecuteNum = %s" % (contactNum, isExecuteNum))
                if contactNum == isExecuteNum:
                    # 如果成功添加的客户数与需要添加的联系人数相等
                    # 说明给第i个用户添加客户信息测试用例执行成功
                    # 在登录账号工作表中写入成功信息，否则写入失败信息
                    excelObj.writeCell(userSheet, "Pass", rowNo=idx + 2, colsNo=account_testResult, style="green")
                else:
                    excelObj.writeCell(userSheet, "Fail", rowNo=idx + 2, colsNo=account_testResult, style="red")
                logging.info("为用户%s添加%d个客户，%d个成功！" % (username, isExecuteNum, contactNum))
            else:
                # 获取被忽略执行的用户名
                ignoreUserName = excelObj.getCellOfValue(userSheet, rowNo=idx + 2, colsNo=account_username)
                logger.info("用户%s被设置为忽略执行！" % ignoreUserName)
            driver.quit()
    except Exception as e:
        logging.info("数据驱动框架主程序发生异常，异常信息为：")
        # 打印异常堆栈信息
        logging.info(traceback.print_exc())
