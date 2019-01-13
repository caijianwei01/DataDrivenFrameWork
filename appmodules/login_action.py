#!/usr/bin/env python
# encoding: utf-8
from pageobjects.login_page import LoginPage


class LoginAction(object):
    def __init__(self):
        print('login...')

    @staticmethod
    def login(i_driver, user_name, pwd):
        try:
            login = LoginPage(i_driver)
            # 将当前焦点切换到登录模块的frame中，以便能进行后续登录操作
            login.switch_to_frame()
            # 输入登录用户名
            login.username_obj().send_keys(user_name)
            # 输入登录密码
            login.password_obj().send_keys(pwd)
            # 单击登录按钮
            login.login_button().click()
            # 切回到默认窗体
            login.switch_to_default_frame()
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver
    import time

    # 启动Chrome浏览器
    driver = webdriver.Chrome(executable_path='D:\zdh\chromedriver.exe')
    # 访问163首页
    driver.get('https://mail.163.com/')
    driver.implicitly_wait(30)
    driver.maximize_window()
    time.sleep(5)
    username = '18367157420'
    password = 'qwer128201209q@'
    LoginAction.login(driver, username, password)
    time.sleep(5)
    driver.quit()
