# -*- encoding: utf-8 -*-
# @Time    : 2018/12/6 18:02
# @Author  : mike.liu
# @File    : VarConfig.py

# 用于定义整个框架中所需要的一些全局常量值，方便维护

# 获取当前文件夹所在目录的父目录的绝对路径
import os

ieDriverFilePath = "E:\Python36\IEDriverServer.exe"
chromeDriverFilePath = "E:\Python36\chromedriver.exe"
firefoxDriverFilePath = "E:\Python36\geckodriver.exe"


parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 存放截图文件
screenPicturesDir = parentDirPath + "\\exceptionpictures"
