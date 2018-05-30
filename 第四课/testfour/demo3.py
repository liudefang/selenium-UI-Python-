# -*- encoding: utf-8 -*-
# @Time    : 2017/12/21 9:38
# @Author  : mike.liu
# @File    : demo3.py
import unittest

#@unittest.skip("无条件跳过此测试类")
class demo(unittest.TestCase):

    @unittest.skip("无条件跳过此用例")
    def test_01(self):
        print("测试无条件跳过此用例")

    @unittest.skipIf(True,"为True的时候跳过")
    def test_02(self):
        print("测试为True的时候跳过")

    @unittest.skipUnless(False,"为False的时候跳过")
    def test_03(self):
        print("测试为False的时候跳过")

    @unittest.expectedFailure
    def test_04(self):
        print("进行断言的时候跳过")
        self.assertEqual(5,8,msg="判断相等")

if __name__ == '__main__':
    unittest.main()