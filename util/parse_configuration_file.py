#!/usr/bin/env python
# encoding: utf-8
from configparser import ConfigParser
from config.var_config import page_element_locator_path


class ParserConfigFile(object):

    def __init__(self):
        self.cf = ConfigParser()
        """
        对于有中文的配置文件，需要指定编码，即加上encoding='uft-8'
        对于有BOM(如Windows下用记事本指定为utf-8)的文件,需要使用 utf-8-sig，即把encoding=utf-8 改为 encoding= utf-8-sig
        """
        self.cf.read(page_element_locator_path, encoding='utf-8')

    def get_items_section(self, section_name):
        """
        :param section_name:section的名称
        :return: 以字典的形式返回section中的所有值
        获取配置文件中指定section下的所有option键值对
        并以字典类型返回调用者
        注意：
        使用self.cf.items(section_name)此种方法获取到的配置文件中的options内容
        均被转换成小写了，比如login_Page.frame被转换成了login_page.frame
        """
        options_dict = dict(self.cf.items(section_name))
        return options_dict

    def get_option_value(self, section_name, option_name):
        """
        :param section_name: section名称
        :param option_name: option名称
        :return:
        获取指定section下的指定option的值
        """
        op_value = self.cf.get(section_name, option_name)
        return op_value


if __name__ == '__main__':
    pc = ParserConfigFile()
    print(pc.get_items_section('163mail_login'))
    sections = pc.get_items_section('163mail_login')
    lo1, lo2 = sections['login_page.iframe'].split('>')
    print(lo1)
    print(lo2)
    print(pc.get_option_value('163mail_login', 'login_page.iframe'))
