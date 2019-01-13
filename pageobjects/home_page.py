#!/usr/bin/env python
# encoding: utf-8
from util import object_map
from util.parse_configuration_file import ParserConfigFile


class HomePage(object):

    def __init__(self, i_driver):
        self.driver = i_driver
        self.parse_cf = ParserConfigFile()

    def address_link(self):
        try:
            # 从定位表达式配置文件中读取定位通讯录按钮的定位方式和表达式
            locator_type, locator_exp = self.parse_cf.get_option_value('163mail_homepage',
                                                                       'homepage.addressbook').split('>')
            element = object_map.get_element(self.driver, locator_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def del_gouxk(self):
        try:
            # 从定位表达式配置文件中读取定位删除勾选框定位方式和表达式
            locator_type, locator_exp = self.parse_cf.get_option_value('163mail_homepage',
                                                                       'homepage.del_gouxk').split('>')
            element = object_map.get_element(self.driver, locator_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def del_delete(self):
        try:
            # 从定位表达式配置文件中读取定位删除文本定位方式和表达式
            locator_type, locator_exp = self.parse_cf.get_option_value('163mail_homepage',
                                                                       'homepage.delete').split('>')
            element = object_map.get_element(self.driver, locator_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def del_confirm(self):
        try:
            # 从定位表达式配置文件中读取定位删除文本定位方式和表达式
            locator_type, locator_exp = self.parse_cf.get_option_value('163mail_homepage',
                                                                       'homepage.confirm').split('>')
            element = object_map.get_element(self.driver, locator_type, locator_exp)
            return element
        except Exception as e:
            raise e
