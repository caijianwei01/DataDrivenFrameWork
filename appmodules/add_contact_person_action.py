#!/usr/bin/env python
# encoding: utf-8
from pageobjects.home_page import HomePage
from pageobjects.address_book_page import AddressBookPage
from time import sleep


class AddContactPerson(object):

    def __init__(self):
        pass

    @staticmethod
    def add(driver, contact_name, contact_email, is_star, contact_phone, contact_comment):
        try:
            # 创建主页实例对象
            hp = HomePage(driver)
            # 单击通讯录链接
            hp.address_link().click()
            # 删除所有已经添加的联系人
            if hp.del_gouxk():
                hp.del_gouxk().click()
                hp.del_delete().click()
                hp.del_confirm().click()
                sleep(2)
            # 创建添加联系人页实例对象
            apb = AddressBookPage(driver)
            apb.create_contact_per_btn().click()
            # 非必填项
            if contact_name:
                apb.contact_person_name().send_keys(contact_name)
            if contact_email:
                apb.contact_person_email().send_keys(contact_email)
            if is_star == u'是':
                apb.star_contacts().click()
            if contact_phone:
                apb.contact_person_mobile().send_keys(contact_phone)
            if contact_comment:
                apb.contact_person_comment().send_keys(contact_comment)
            apb.save_contace_person().click()
        except Exception as e:
            raise e


if __name__ == '__main__':
    from appmodules.login_action import LoginAction
    from selenium import webdriver
    import time

    driver = webdriver.Chrome(executable_path='D:\zdh\chromedriver.exe')
    driver.get('https://mail.163.com/')
    driver.maximize_window()
    LoginAction.login(driver, '18367157420', 'qwer128201209q@')
    AddContactPerson.add(driver, '紫陌翌晨', '1031901787@qq.com', '是', '18367157420', '知心好友')
    time.sleep(5)
    assert '紫陌翌晨' in driver.page_source
    time.sleep(5)
    driver.quit()
