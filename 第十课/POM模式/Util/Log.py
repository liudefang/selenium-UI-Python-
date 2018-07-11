# -*- encoding: utf-8 -*-
# @Time    : 2018/7/7 10:27
# @Author  : mike.liu
# @File    : Log.py

import logging.config
from config.VarConfig import parentDirPath

logging.config.fileConfig(parentDirPath + "\config\Logger.conf")

# 选择一个日志格式
logger = logging.getLogger("example02")


def debug(message):
    # 定义debug级别日志打印方法
    logger.debug(message)


def info(message):
    # 定义info级别日志打印方法
    logger.info(message)


def warning(message):
    # 定义warning级别日志打印方法
    logger.warning(message)