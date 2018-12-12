# -*- encoding: utf-8 -*-
# @Time    : 2018/12/6 18:03
# @Author  : mike.liu
# @File    : DirAndTime.py


# 获取当前的日期
import datetime
import os
import time

from 第十三课.KeyWorkFrameWorkDemo.config.VarConfig import screenPicturesDir


def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) + "-" + str(timeTup.tm_mon) + "-" + str(timeTup.tm_mday)
    return currentDate


# 获取当前的时间
def getCurrentTime():
    timeStr = datetime.datetime.now()
    nowTime = timeStr.strftime('%H-%M-%S-%f')
    return nowTime


# 创建截图存放的目录
def createCurrentDateDir():
    dirName = os.path.join(screenPicturesDir, getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName
