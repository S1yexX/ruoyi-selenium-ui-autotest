import time

from selenium.webdriver.support.select import Select

from bases.base_page import BasePage


class UserList(BasePage):
    # 写导航页面的属性（元素定位）
    system_a_loc = "//*[text()='系统管理']"
    user_a_loc = "//a[@data-index='3']"
    login_name_loc ="//input[@name='loginName']"
    phone_num_loc ="//input[@name='phonenumber']"
    status_id_loc = "//select[@name='status']"
    tableSearch_a_loc = "//a[@onclick='$.table.search()']"
    edit_a_loc = '//a[@onclick="$.operate.editTab(\'2\')"]'

    # 写登陆页面的方法（操作）
    def switch_to_frame(self):
        self.goto_frame(self.system_a_loc,self.user_a_loc)

    # 输入登录名称
    def input_name_by_value(self, login_name):
        self.find_ele(self.login_name_loc).send_keys(login_name)

    # 输入手机号码
    def input_phone_num_by_value(self, phone_num):
        self.find_ele(self.phone_num_loc).send_keys(phone_num)

    # 操作下拉框
    def select_by_value(self, value):
        ele = Select(self.find_ele(self.status_id_loc))
        ele.select_by_value(value)

    # 点击搜索按钮
    def click_search(self):
        self.find_ele(self.tableSearch_a_loc).click()

    # 点击编辑按钮
    def click_edit(self):
        time.sleep(1)
        self.find_ele(self.edit_a_loc).click()
