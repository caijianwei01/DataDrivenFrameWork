#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from pageobjects.login_page import LoginPage
import time


def test_mail_login():
    try:
        # 启动浏览器
        driver = webdriver.Chrome(executable_path='D:\zdh\chromedriver.exe')
        # 访问163邮箱首页
        url = 'https://mail.163.com/'
        driver.get(url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(5)
        login = LoginPage(driver)
        # 将当前焦点切换到登录模块的frame中，以便能进行后续登录操作
        login.switch_to_frame()
        # 输入登录用户名
        login.username_obj().send_keys('18367157420')
        # 输入登录密码
        login.password_obj().send_keys('qwer128201209q@')
        # 单击登录按钮
        login.login_button().click()
        time.sleep(5)
        # 切换到默认窗体，以兼容chrome浏览器
        login.switch_to_default_frame()
        assert '未读邮件' in driver.page_source
    except Exception as e:
        raise e
    finally:
        # 退出浏览器
        driver.quit()


if __name__ == '__main__':
    test_mail_login()
    print('登录163邮箱成功！')
