#!/usr/bin/env python
# encoding: utf-8
'''
用于实现定位页面元素的公共方法
'''
from selenium.webdriver.support.ui import WebDriverWait


# 获取单个页面元素对象
def get_element(i_driver, locate_type, locator_expression):
    try:
        # 采用显示等待，并且默认每0.5秒查询一次
        element = WebDriverWait(i_driver, 10).until(lambda x: x.find_element(by=locate_type, value=locator_expression))
        return element
    except Exception:
        return None


# 获取单个页面多个元素对象，以list返回
def get_elements(i_driver, locate_type, locator_expression):
    try:
        elements = WebDriverWait(i_driver, 20).until(
            lambda x: x.find_elements(by=locate_type, value=locator_expression))
        return elements
    except Exception:
        return None


if __name__ == '__main__':
    from selenium import webdriver

    # 进行单元测试
    driver = webdriver.Chrome(executable_path="D:\zdh\chromedriver.exe")
    driver.get('https://www.baidu.com/')
    driver.find_elements()

    search_box = get_element(driver, 'id', 'kw')
    # 打印页面对象的标签名
    search_box.send_keys('cjw')
    print(search_box.tag_name)
    a_list = get_elements(driver, 'tag name', 'a')
    print(len(a_list))
    driver.quit()
