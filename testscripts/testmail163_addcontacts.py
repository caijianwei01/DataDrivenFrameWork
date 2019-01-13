#!/usr/bin/env python
# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.parse_excel import ParseExcel
from config.var_config import *
from appmodules.login_action import LoginAction
from appmodules.add_contact_person_action import AddContactPerson
from time import sleep
from util.Log import *
import traceback

# 创建解析Excel对象
excelObj = ParseExcel()
# 将Excel数据文件加载到内存
excelObj.load_workbook(data_file_path)


def launch_browser():
    # 创建Chrome浏览器的一个Options实例对象
    chrome_options = Options()
    # 向Options实例中添加禁用扩展插件的设置参数项
    chrome_options.add_argument('--disable-extensions')
    # 添加屏蔽--ignore-certificate-errors提示信息的设置参数项
    chrome_options.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
    # 添加浏览器最大化的设置参数项，已启动就最大化
    chrome_options.add_argument('--start-maximized')
    # 启动带有自定义设置的Chrome浏览器
    driver = webdriver.Chrome(executable_path='D:\zdh\chromedriver.exe', chrome_options=chrome_options)
    # 访问163邮箱首页
    driver.get('https://mail.163.com')
    sleep(3)
    return driver


def test_163_mail_add_contacts():
    logging.info('163邮箱添加联系人数据驱动测试开始...')
    try:
        # 根据Excel文件中sheet名称获取此sheet对象
        user_sheet = excelObj.get_sheet_by_name('163账号')
        # 获取163账号sheet中是否执行列
        is_execute_user = excelObj.get_column(user_sheet, account_isExecute - 1)
        # 获取163账号sheet中的数据列
        data_book_col = excelObj.get_column(user_sheet, account_dataBook - 1)
        # 创建浏览器实例对象
        driver = launch_browser()
        logging.info('启动浏览器，访问163邮箱主页')
        for idx, value in enumerate(is_execute_user[1:]):
            if value == 'y':  # 表示要执行
                # 循环遍历163账号表中的账号，为需要执行的账号添加联系人
                user_row = excelObj.get_row(user_sheet, idx + 1)
                # 获取第i行中的用户名
                username = user_row[account_username - 1]
                # 获取第i行中的密码
                password = user_row[account_password - 1]
                logging.info('测试用户名：%s, 测试用户密码：%s' % (username, password))

                # 登录163邮箱
                LoginAction.login(driver, username, password)
                # 等待3秒，让浏览器启动完成，以便正常进行后续操作
                sleep(3)
                try:
                    # 断言登录后跳转页面的标题是否包含‘网易邮箱’
                    assert '收 信' in driver.page_source
                    logging.info('用户 %s 登录后，断言页面关键字"收 信"成功' % username)
                except AssertionError:
                    logging.debug('用户 %s 登录后，断言页面关键字"收 信"失败, 异常信息：%s'
                                  % (username, str(traceback.format_exc())))
                # 获取第i行中用户添加的联系人数据表sheet名
                data_book_name = data_book_col[idx + 1]
                # 获取对应的数据表对象
                data_sheet = excelObj.get_sheet_by_name(data_book_name)
                # 获取联系人数据表中是否执行列对象
                is_execute_data = excelObj.get_column(data_sheet, contacts_isExecute - 1)
                contact_num = 0  # 记录添加成功联系人个数
                is_execute_num = 0  # 记录需要执行联系人个数
                for inx, data in enumerate(is_execute_data[1:]):
                    # 循环遍历是否执行添加联系人列，如果被设置为添加，则进行联系人添加操作
                    if data == 'y':  # 表示要执行
                        # 如果第id行的联系人被设置为执行，则is_execute_num自增1
                        is_execute_num += 1
                        # 获取联系人表第id+1行对象
                        row_content = excelObj.get_row(data_sheet, inx + 1)
                        # 获取联系人姓名
                        contact_person_name = row_content[contacts_contactPersonName - 1]
                        # 获取联系人邮箱
                        contact_person_email = row_content[contacts_contactPersonEmail - 1]
                        # 获取是否设置为星标联系人
                        is_star = row_content[contacts_isStar - 1]
                        # 获取联系人手机号
                        contact_person_phone = row_content[contacts_contactPersonMobile - 1]
                        # 获取联系人备注信息
                        contact_person_comment = row_content[contacts_contactPersonComment - 1]
                        if contact_person_comment == 'None':
                            contact_person_comment = None
                        # 获取添加联系人成功后，断言的关键字
                        assert_key_word = row_content[contacts_assertKeyWords - 1]
                        # 执行新建联系人操作
                        AddContactPerson.add(driver, contact_person_name, contact_person_email, is_star,
                                             contact_person_phone, contact_person_comment)
                        sleep(2)
                        logging.info('添加联系人 %s 成功' % contact_person_email)
                        # 在联系人工作表中添加联系人执行时间
                        excelObj.write_cell_current_time(data_sheet, row_no=inx + 2, col_no=contacts_runTime)
                        try:
                            # 断言给定的关键字是否出现在页面中
                            assert assert_key_word in driver.page_source
                        except AssertionError:
                            # 断言失败，在联系人工作表中写入添加联系人测试失败信息
                            excelObj.write_cell(data_sheet, 'failed', row_no=inx + 2, col_no=contacts_testResult,
                                                style='red')
                            logging.info('断言关键字 "%s" 失败' % assert_key_word)
                        else:
                            # 断言成功，写入添加联系人成功信息
                            excelObj.write_cell(data_sheet, 'pass', row_no=inx + 2, col_no=contacts_testResult,
                                                style='green')
                            logging.info('断言关键字 "%s" 成功' % assert_key_word)
                            contact_num += 1
                    elif data == 'n':
                        # 获取被忽略执行的联系人
                        row_content = excelObj.get_row(data_sheet, inx + 1)
                        contact_person_email = row_content[contacts_contactPersonEmail - 1]
                        logging.info('联系人 %s 被忽略执行' % contact_person_email)
                if contact_num == is_execute_num:
                    # 如果成功添加的联系人个数与需要添加的联系人数相等，
                    # 说明给第i个用户添加联系人测试用例执行成功，
                    # 在163账号工作表中写入成功信息，否则写入失败信息
                    excelObj.write_cell(user_sheet, 'pass', row_no=idx + 2, col_no=account_testResult, style='green')
                else:
                    excelObj.write_cell(user_sheet, 'failed', row_no=idx + 2, col_no=account_testResult, style='red')
                logging.info('为用户 %s 添加%d个联系人, %d个成功\n' % (username, is_execute_num, contact_num))
            elif value == 'n':
                ignore_user_name = excelObj.get_cell_of_value(user_sheet, row_no=idx + 2, col_no=account_username)
                logging.info('用户 %s 被忽略执行\n' % ignore_user_name)
            driver.quit()
    except Exception as e:
        logging.info('数据驱动框架主程序执行过程发生异常，异常信息：%s' % str(traceback.format_exc()))


if __name__ == '__main__':
    test_163_mail_add_contacts()
