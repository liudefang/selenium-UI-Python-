# -*- encoding: utf-8 -*-
# @Time    : 2018/8/30 17:54
# @Author  : mike.liu
# @File    : AddCustomerAction.py
import time
import traceback

from 第十二课.DataDrivenFrameWork.pageObject.CustomerPage import CustomerPage


class AddCustomer(object):
    def __init__(self):
        print("添加客户信息")

    @staticmethod
    def customer(driver, customerUserName, customerPhoneNumber):
        try:
            # 新建添加客户资料的对象
            cp = CustomerPage(driver)
            # 点击财富中心客户菜单
            cp.fortuneCenter().click()
            time.sleep(5)
            # 切换入添加客户资料页面的fram
            cp.fram()
            # 点击添加按钮
            cp.addLink().click()
            time.sleep(3)
            # 输入客户姓名
            cp.userName().send_keys(customerUserName)
            # 选择记录类型
            cp.recordType().click()
            # 选择获取方式
            cp.fromType().click()
            # 选择性别
            cp.sex().click()
            # 选择预约类型
            cp.ctype().click()
            # 输入手机号码
            cp.phoneNumber().send_keys(customerPhoneNumber)
            # 输入预约时间
            cp.yytime().click()
            time.sleep(3)
            # 切换出当前fram，进入到日期选择fram
            cp.tofram()
            # 进入到日期的ifram里面
            cp.ifram()
            # 选择今天
            cp.dpTodayInput().click()
           # 切换出日期的ifram
            cp.tofram()
            time.sleep(3)
            # 进入到新建客户的ifram里面
            cp.fram()
            # 点击保存按钮
            cp.saveCustomer().click()
            time.sleep(5)
            # # 切换出添加客户的ifram
            # cp.tofram()
            # time.sleep(2)
            # # 切换入添加客户资料页面的fram
            # cp.fram()
        except Exception as e:
            # 打印堆栈异常信息
            print(traceback.print_exc())
            raise e
