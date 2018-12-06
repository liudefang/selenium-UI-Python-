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
