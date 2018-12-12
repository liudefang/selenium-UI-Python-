# -*- encoding: utf-8 -*-
# @Time    : 2018/11/23 16:00
# @Author  : mike.liu
# @File    : VarConfig.py
import os

ieDriverFilePath = "E:\Python36\IEDriverServer.exe"
chromeDriverFilePath = "E:\Python36\chromedriver.exe"
firefoxDriverFilePath = "E:\Python36\geckodriver.exe"

# 获取当前文件夹所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 存放截图文件
screenPicturesDir = parentDirPath + "\\exceptionpictures"

# 测试数据文件存放绝对路径
dataFilePath = parentDirPath + "\\testData\\关键字驱动测试用例.xlsx"

# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName = 2
testCase_testStepSheetName = 4
testCase_isExecute = 5
testCase_runTime = 6
testCase_testResult = 7


# 用例步骤表中，部分对应的数字序号
testStep_testStepDescribe = 2
testStep_keyWords = 3
testStep_locationType = 4
testStep_locatorExpression = 5
testStep_operateValue = 6
testStep_runTime = 7
testStep_testResult = 8
testStep_errorInfo = 9
testStep_errorPic = 10