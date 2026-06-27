from bases.base_page import BasePage


class LoginPage(BasePage):

    # 写导航页面的属性（元素定位）
    validateCode_loc = "//input[@name='validateCode']"
    submit_loc = "//button[@id='btnSubmit']"

    # 写登陆页面的方法（操作）
    def login(self,code):
            self.find_ele(self.validateCode_loc).send_keys(code)
            self.find_ele(self.submit_loc).click()
