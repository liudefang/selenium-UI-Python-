# -*- encoding: utf-8 -*-
# @Time    : 2018/8/6 18:09
# @Author  : mike.liu
# @File    : ParseConfigurationFile.py

# 用于解析存储定位页面元素的定位表达式文件，以便获取定位表达式
from configparser import ConfigParser

from config.VarConfig import pageElementLocatorPath


class ParseConfigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self, sectionName):
        # 获取配置文件中指定section下面的所有option键值对
        # 并以字典类型返回给调用者
        """注意：
        使用self.cf.items(sectionName)此种方法获取到的配置文件中
        的options内容均被转换成小写，
        比如LoginPage.frame 被转换成了LoginPage.frame """
        optionsDir = dict(self.cf.items(sectionName))
        return optionsDir

    def getOptionValue(self, sectionName, optionName):
        # 获取指定section下面的指定option的值
        value = self.cf.get(sectionName, optionName)
        return value

if __name__ == '__main__':
    pc = ParseConfigFile()
    print(pc.getItemsSection("erp_login"))
    print(pc.getOptionValue("erp_login", "loginPage.username"))