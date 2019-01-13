#!/usr/bin/env python
# encoding: utf-8
'''
登录页面
'''
from util import object_map
from util.parse_configuration_file import ParserConfigFile


class LoginPage(object):

    def __init__(self, i_driver):
        self.driver = i_driver
        self.parse_cf = ParserConfigFile()
        self.login_options = self.parse_cf.get_items_section('163mail_login')

    def switch_to_frame(self):
        try:
            # 从定位表达式配置文件中读取frame的定位表达式
            locator_type, locator_exp = self.login_options['login_page.iframe'].split('>')
            frame = object_map.get_element(self.driver, locator_type, locator_exp)
            self.driver.switch_to.frame(frame)
        except Exception as e:
            raise e

    def switch_to_default_frame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    # 用户名
    def username_obj(self):
        try:
            # 从定位表达式配置文件中读取定位用户名输入框的定位方式和表达式
            locator_type, locator_exp = self.login_options['login_page.username'].split('>')
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            element = object_map.get_element(self.driver, locator_type, locator_exp)
            return element
        except Exception as e:
            raise e

    # 密码
    def password_obj(self):
        try:
            # 从定位表达式配置文件中读取定位密码输入框的定位方式和表达式
            locator_type, locator_exp = self.login_options['login_page.password'].split('>')
            # 获取页面的密码输入框页面对象，并返回给调用者
            element = object_map.get_element(self.driver, locator_type, locator_exp)
            return element
        except Exception as e:
            raise e

    # 登录按钮
    def login_button(self):
        try:
            # 从定位表达式配置文件中读取定位密码输入框的定位方式和表达式
            locator_type, locator_exp = self.login_options['login_page.loginbuttom'].split('>')
            # 获取登录页面的登录按钮页面对象，并返回给调用者
            element = object_map.get_element(self.driver, locator_type, locator_exp)
            return element
        except Exception as e:
            raise e


if __name__ == '__main__':
    # 测试代码
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path='D:\zdh\chromedriver.exe')
    driver.get('https://mail.163.com/')
    import time

    time.sleep(2)
    login = LoginPage(driver)
    login.switch_to_frame()
    # 输入用户名
    login.username_obj().send_keys('18367157420')
    # 输入密码
    login.password_obj().send_keys('qwer128201209q@')
    login.login_button().click()
    login.switch_to_default_frame()
    time.sleep(3)
    assert '未读邮件' in driver.page_source
    driver.quit()
