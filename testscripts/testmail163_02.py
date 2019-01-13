#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from appmodules.login_action import LoginAction
import time


def test_mail_login():
    try:
        # 启动Chrome浏览器
        driver = webdriver.Chrome('D:\zdh\chromedriver.exe')
        # 访问163邮箱首页
        driver.get('https://mail.163.com')
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(2)
        # 登录163邮箱
        LoginAction.login(driver, '18367157420', 'qwer128201209q@')
        time.sleep(5)
        assert '未读邮件' in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()


if __name__ == '__main__':
    test_mail_login()
    print('登录163邮箱成功！')
