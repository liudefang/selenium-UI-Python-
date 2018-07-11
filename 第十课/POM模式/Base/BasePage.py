# -*- encoding: utf-8 -*-
# @Time    : 2018/7/5 20:00
# @Author  : mike.liu
# @File    : BasePage.py

# 定义全局driver变量
import time

from selenium.common.exceptions import NoSuchElementException

from Util.Log import logger

driver = None
# 全局的等待类实例对象
waitUtil = None


class Action(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    # 初始化driver，URL
    def __init__(self, driver):
        self.driver = driver

    # 定位元素方法
    def find_element(self, selctor):
        """
        这个地方为什么根据=>来切割字符串，请看页面里定位元素的方法
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selctor:
        :return:
        """
        element = ''
        if '=>' not in selctor:
            return self.driver.find_element_by_id(selctor)
        selctor_by = selctor.split('=>')[0]
        selctor_value = selctor.split('=>')[1]

        if selctor_by == "i" or selctor_by == "id":
            try:
                element = self.driver.find_element_by_id(selctor_value)
                logger.info("找到了元素 %s 成功" "%s 该值为: %s" % (element.text, selctor_by, selctor_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selctor_by == "n" or selctor_by == "name":
            element = self.driver.find_element_by_name(selctor_value)
        elif selctor_by == "class" or selctor_by == "class_name":
            element = self.driver.find_element_by_class_name(selctor_value)
        elif selctor_by == "link" or selctor_by == "link_text":
            element = self.driver.find_element_by_link_text(selctor_value)
        elif selctor_by == "partial" or selctor_by == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(selctor_value)
        elif selctor_by == "tag" or selctor_by == "tag_name":
            element = self.driver.find_element_by_tag_name(selctor_value)
        elif selctor_by == "x" or selctor_by == "xpath":
            try:
                element = self.driver.find_element_by_xpath(selctor_value)
                logger.info("找到了元素 %s 成功" "%s 该值为: %s" % (element.text, selctor_by, selctor_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
        elif selctor_by == "s" or selctor_by == "selector_selector":
            element = self.driver.find_element_by_css_selector(selctor_value)
        else:
            raise NameError("请输入有效的定位元素类型")
        return element

    # 输入
    def input_string(self, selector, inputContent):
        try:
            self.find_element(selector).send_keys(inputContent)
            logger.info("在输入框输入 %s" % inputContent)
        except NameError as e:
            logger.error("输入框无法输入 %s" % inputContent)

    # 点击操作
    def click(self, selector):
        try:
            self.find_element(selector).click()
            logger.info("点击该按钮成功")
        except NameError as e:
            logger.info("点击该按钮失败")

    # 获取网页标题
    def get_page_title(self):
        logger.info("获取网页的标题是:%s" % self.driver.title)
        return self.driver.title

    def assert_string_in_pagesource(self, assertString):
        # 断言页面源码是否存在某关键字或关键字字符串

        try:
            assert assertString in self.driver.page_source, "%s not found in page source!" % assertString
            logger.info("查找预期结果成功，%s" % assertString)
        except AssertionError as e:
            raise AssertionError(e)
        except Exception as e:
            raise e

    # 等待时间
    def sleep(self, seconds):
        time.sleep(seconds)
        logger.info("等待 %s 秒" % seconds)

    # 关闭浏览器
    def close_browser(self):
        # 关闭浏览器

        try:
            self.driver.quit()
        except Exception as e:
            raise e


