# -*- encoding: utf-8 -*-
# @Time    : 2017/12/20 18:02
# @Author  : mike.liu
# @File    : run_all_case.py
import smtplib
import unittest

import os

import time
from HTMLTestRunner import HTMLTestRunner



#发送邮箱服务器
from email.header import Header
from email.mime.text import MIMEText

smtpserver = 'smtp.163.com'
#发送邮箱用户/密码
user = '15989576517@163.com'
password = '*****'
#发送邮箱
sender = '15989576517@163.com'
#接收邮箱
receiver = '15989576517@139.com'
#发送邮件主题
subject = '自动化测试'
#============定义发送邮件=============
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '<15989576517@163.com>'
    msg['To'] = '<15989576517@139.com>'


    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('email has send out!')

#======查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    result_dir = 'D:\\pythonpj\\testfour\\report'

    lists = os.listdir(result_dir)

    # 重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    print(('最新的文件为:' + lists[-1]))
    file_new = os.path.join(result_dir, lists[-1])
    print(file_new)
    return file_new

#用例路径
case_path = os.path.join(os.getcwd(),"testcase")

#报告存放路径
report_path = os.path.join(os.getcwd(),"report")


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)

    print("discover")

    return discover


if __name__ == '__main__':
    #unittest.main()       #启动单元测试


    #按照一定格式获取当前时间
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")

    #定义报告存放路径
    filename = report_path + '/' + nowTime + 'result.html'
    fp = open(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,title='UI自动化测试用例',description='用例执行情况:',verbosity=2)
    runner.run(all_case())   #运行测试用例
    fp.close()  #关闭报告文件

new_report = new_report(report_path)
send_mail(new_report)
