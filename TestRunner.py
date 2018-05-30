# -*- encoding: utf-8 -*-
# @Time    : 2017/12/25 14:31
# @Author  : mike.liu
# @File    : TestRunner.py
import unittest

from testcase.test_chromeTest import BrowserTest



if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_firefox('test_chrome'))
    suite.addTest(BrowserTest('test_firefox'))
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)