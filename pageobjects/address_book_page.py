#!/usr/bin/env python
# encoding: utf-8
from util.object_map import *
from util.parse_configuration_file import ParserConfigFile


class AddressBookPage(object):

    def __init__(self, i_driver):
        self.driver = i_driver
        self.parser_cf = ParserConfigFile()
        self.cts_options = self.parser_cf.get_items_section('163mail_add_contacts_page')

    def create_contact_per_btn(self):
        """
        获取新建联系人按钮
        """
        try:
            # 从定位表达式配置文件中读取定位新建联系人按钮的定位方式和表达式
            locate_type, locator_exp = self.cts_options['add_contacts_page.create_contacts_btn'].split('>')
            # 获取新建联系人按钮页面元素，并返回给调用者
            element = get_element(self.driver, locate_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def contact_person_name(self):
        """
        获取新建联系人界面中的姓名输入框
        """
        try:
            # 从定位表达式配置文件中读取新建联系人姓名输入框的定位方式和表达式
            locate_type, locator_exp = self.cts_options['add_contacts_page.contact_person_name'].split('>')
            # 获取新建联系人界面的姓名输入框页面元素，并返回给调用者
            element = get_element(self.driver, locate_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def contact_person_email(self):
        """
        获取新建联系人界面中的电子邮件输入框
        """
        try:
            # 从定位表达式配置文件中读取联系人邮件输入框的定位方式和表达式
            locate_type, locator_exp = self.cts_options['add_contacts_page.contact_person_email'].split('>')
            # 获取新建联系人界面的邮箱输入框页面元素，并返回给调用者
            element = get_element(self.driver, locate_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def star_contacts(self):
        """
        获取新建联系人界面中的星标联系人选择框
        """
        try:
            # 从定位表达式配置文件中读取星标联系人复选框的定位方式和表达式
            locate_type, locator_exp = self.cts_options['add_contacts_page.star_contacts'].split('>')
            # 获取新建联系人界面的星标联系人复选框页面元素，并返回给调用者
            element = get_element(self.driver, locate_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def contact_person_mobile(self):
        """
        获取新建联系人界面中的联系人手机号输入框
        """
        try:
            # 从定位表达式配置文件中读取联系人手机号输入框的定位方式和表达式
            locate_type, locator_exp = self.cts_options['add_contacts_page.contact_person_mobile'].split('>')
            # 获取新建联系人界面的联系人手机号输入框页面元素，并返回给调用者
            element = get_element(self.driver, locate_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def contact_person_comment(self):
        """
        获取新建联系人界面中的联系人备注信息输入框
        """
        try:
            # 从定位表达式配置文件中读取联系人备注信息输入框定位方式和表达式
            locate_type, locator_exp = self.cts_options['add_contacts_page.contact_person_comment'].split('>')
            # 获取新建联系人界面中备注信息输入框页面元素，并返回给调用者
            element = get_element(self.driver, locate_type, locator_exp)
            return element
        except Exception as e:
            raise e

    def save_contace_person(self):
        """
        获取新建联系人界面中的保存联系人按钮
        """
        try:
            # 从定位表达式配置文件中读取保存联系人按钮的定位方式和表达式
            locate_type, locator_exp = self.cts_options['add_contacts_page.save_contace_person'].split('>')
            # 获取新建联系人界面的保存联系人按钮页面元素，并返回给调用者
            element = get_element(self.driver, locate_type, locator_exp)
            return element
        except Exception as e:
            raise e
