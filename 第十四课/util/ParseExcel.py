# -*- encoding: utf-8 -*-
# @Time    : 2018/12/5 8:59
# @Author  : mike.liu
# @File    : ParseExcel.py
from openpyxl.styles import Font


class ParseExcel(object):
    def __init__(self):
        self.workbook = None
        self.excelFile = None
        self.font = Font(color=None)        # 设置字体颜色
        # 颜色对于的RGB值
        self.RGBDict = {'red': 'FFFF3030', 'green': 'FF008B00'}

    def loadWorkBook(self.excelPathAndName):
