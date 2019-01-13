#!/usr/bin/env python
# encoding: utf-8
'''
此文件主要用于定义一些全局变量，用于存储一些文件路径等
'''
import os

# 获取当前文件所在目录的绝对路径
parent_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取存放页面元素定位表达式文件的绝对路径
page_element_locator_path = parent_dir_path + '\\config\\page_element_locator.ini'

# 获取数据文件存放绝对路径
# data_file_path = parent_dir_path + u'\\testdata\\163邮件联系人.xlsx'
data_file_path = r'D:\zdh\163邮箱联系人.xlsx'

# 163账号工作表中，每列对应的数字序号。注意：列号和行号都是从0开始的
account_username = 2
account_password = 3
account_dataBook = 4
account_isExecute = 5
account_testResult = 6

# 联系人工作表中，每列对应的数字序号
contacts_contactPersonName = 2
contacts_contactPersonEmail = 3
contacts_isStar = 4
contacts_contactPersonMobile = 5
contacts_contactPersonComment = 6
contacts_assertKeyWords = 7
contacts_isExecute = 8
contacts_runTime = 9
contacts_testResult = 10
