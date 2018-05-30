# -*- encoding: utf-8 -*-
# @Time    : 2017/12/20 15:27
# @Author  : mike.liu
# @File    : demo1.py

import unittest
class testdemo(unittest.TestCase):

    def setUp(self):
        '''测试固件setUp的代码，主要用于测试的前期准备工作'''
        print("start!")
    def tearDown(self):
        '''测试结束之后的清理，一般是关闭浏览器'''

        print("end!")

    def test_demo01(self):
        '''这里一定要以test开头'''
        print("执行demo测试用例A")

    def test_demo03(self):
        '''这里一定要以test开头'''
        print("执行demo测试用例C")

    def test_demo02(self):
        '''这里一定要以test开头'''
        print("执行demo测试用例B")

    def addtest(self):
        print("addtest方法")


if __name__ == '__main__':
    unittest.main()