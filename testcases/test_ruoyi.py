import allure
import pytest

from commons.excel_utils import read_excel_to_list
from poms.user_list import UserList


@allure.epic("项目名称：若依网站自动化测试框架")
class TestRuoyi:
    # def test_login(self,all_case_fixture):
    #     #手动输入验证码
    #     code = input("请输入验证码:")
    #     #登录
    #     LoginPage(all_case_fixture).login(code)
    #===============================================================
    #
    #     # 不让浏览器自动关闭
    #     options = webdriver.EdgeOptions()
    #     options.add_experimental_option("detach", True)
    #
    #     # 创建浏览器对象
    #     driver = webdriver.Edge(options=options)
    #
    #     #加载项目地址
    #     driver.get("https://demo.ruoyi.vip/login")
    #
    #     # 定位
    #
    #     #输入用户名
    #     #driver.find_element(By.XPATH, "//input[@name='username']").send_keys("admin")
    #
    #     #输入密码
    #     #driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    #
    #     # 手动输入验证码
    #     r = input("请输入验证码：")
    #
    #     # 输入验证码
    #     driver.find_element(By.XPATH, "//input[@name='validateCode']").send_keys(r)
    #
    #     # 点击登录按钮
    #     driver.find_element(By.XPATH, "//button[@id='btnSubmit']").click()

    # def test_select_user(self,all_case_fixture):
        # # 手动输入验证码
        # code = input("请输入验证码:")
        # # 登录
        # LoginPage(all_case_fixture).login(code)

        # 给返回的driver赋值
        # driver = all_case_fixture

        # 页面睡眠3秒
        # time.sleep(3)

        # # 点击系统管理列表
        # driver.find_element(By.XPATH, "//*[text()='系统管理']").click()
        #
        # # 点击用户管理列表
        # driver.find_element(By.XPATH, "//*[text()='用户管理']").click()
        #
        # # 进入框架
        # driver.switch_to.frame("iframe3")

        # 页面睡眠3秒
        # time.sleep(3)

        # # 操作下拉框
        # ele = driver.find_element(By.XPATH,"//select[@name='status']")
        # sel_ele = Select(ele)
        # #sel_ele.select_by_index(2)
        # sel_ele.select_by_value("0")
        # #sel_ele.select_by_visible_text("停用")

        # # 点击搜索
        # driver.find_element(By.XPATH, "//a[@onclick='$.table.search()']").click()



        # 页面睡眠3秒
        # time.sleep(3)

        # # 点击编辑按钮
        # driver.find_element(By.XPATH,"//*[text()='编辑']").click()

    # def test_add_user(self,all_case_fixture):
        # # 手动输入验证码
        # code = input("请输入验证码:")
        # # 登录
        # LoginPage(all_case_fixture).login(code)

        # 给返回的driver赋值
        # driver = all_case_fixture

        # 页面睡眠3秒
        # time.sleep(3)

        # # 点击系统管理列表
        # driver.find_element(By.XPATH, "//*[text()='系统管理']").click()
        #
        # # 点击用户管理列表
        # driver.find_element(By.XPATH, "//*[text()='用户管理']").click()
        #
        # # 进入框架
        # driver.switch_to.frame("iframe3")

        # # 页面睡眠3秒
        # time.sleep(3)
        #
        # # 操作下拉框
        # ele = driver.find_element(By.XPATH, "//select[@name='status']")
        # sel_ele = Select(ele)
        # # sel_ele.select_by_index(2)
        # sel_ele.select_by_value("0")
        # # sel_ele.select_by_visible_text("停用")
        #
        # # 点击搜索
        # driver.find_element(By.XPATH, "//a[@onclick='$.table.search()']").click()
        #
        # # 页面睡眠3秒
        # time.sleep(3)
        #
        # # 点击新增按钮
        # driver.find_element(By.XPATH, "//a[@onclick='$.operate.addTab()']").click()
        #
        # # 页面睡眠3秒
        # time.sleep(3)
        #
        # # 出框架
        # driver.switch_to.default_content()
        #
        # # 进入框架
        # # 正确xpath，class精准匹配 + data-id精准匹配
        # frame = driver.find_element(By.XPATH, '//iframe[@data-id="/system/user/add"]')
        # driver.switch_to.frame(frame)
        #
        # # 页面睡眠3秒
        # time.sleep(3)
        #
        # # 输入商品名称
        # driver.find_element(By.XPATH,"//input[@name='userName']").send_keys("user")
        #
        # # 选择归属部门
        # driver.find_element(By.XPATH,"//input[@onclick='selectDeptTree()']").click()
        #
        # # 页面睡眠3秒
        # time.sleep(3)
        #
        # # 出框架
        # driver.switch_to.default_content()
        #
        # # 进入框架
        # dept_frame = driver.find_element(By.XPATH, '//iframe[starts-with(@id, "layui-layer-iframe")]')
        # driver.switch_to.frame(dept_frame)
        #
        # # 页面睡眠3秒
        # time.sleep(3)
        #
        # # 点击研发部门
        # driver.find_element(By.XPATH, "//a[@id='tree_3_a']").click()
        #
        # # 页面睡眠3秒
        # time.sleep(3)
        #
        # # 出框架
        # driver.switch_to.default_content()
        #
        # # 点击确认
        # driver.find_element(By.XPATH, "//div[@class='layui-layer-btn']").click()
        #
        # # 出框架
        # driver.switch_to.default_content()
        #
        # # 进入框架
        # # 正确xpath，class精准匹配 + data-id精准匹配
        # frame = driver.find_element(By.XPATH, '//iframe[@data-id="/system/user/add"]')
        # driver.switch_to.frame(frame)
        #
        # # 输入手机号
        # driver.find_element(By.XPATH, "//input[@name='phonenumber']").send_keys("18026472661")
        #
        # # 输入邮箱
        # driver.find_element(By.XPATH, "//input[@name='email']").send_keys("1006225709@qq.com")
        #
        # # 输入登录账号
        # driver.find_element(By.XPATH, "//input[@name='loginName']").send_keys("user01")
        #
        # # 输入密码
        # driver.find_element(By.XPATH, "//input[@name='password']").clear()
        # driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456")
        #
        # # 选择性别
        # sel = Select(driver.find_element(By.XPATH, "//select[@name='sex']"))
        # sel.select_by_value("1")
        #
        # # 选择岗位
        # sel = Select(driver.find_element(By.XPATH, "//select[@id='post']"))
        # sel.select_by_value("1")
        #
        # # 输入备注
        # driver.find_element(By.XPATH, "//textarea[@name='remark']").send_keys("黄总")
        #
        # # 点击保存
        # driver.find_element(By.XPATH,"//button[@onclick='submitHandler()']").click()

    # 定制Allure报告
    @allure.epic('自动化测试')
    @allure.feature('项目名称：用户管理')
    @allure.story('页面名称：用户列表')
    @allure.title('"用例名称： " + caseinfo["case_name"]')
    #POM封装应用
    @pytest.mark.parametrize("caseinfo", read_excel_to_list(r"./testcases/select_user.xlsx", "select_user"))
    def test_select_user(self, all_case_fixture, caseinfo):

        print(caseinfo)
        sl = UserList(all_case_fixture)
        sl.switch_to_frame()
        if str(caseinfo["loginName"]) != "nan":
            sl.input_name_by_value(str(caseinfo["loginName"]))
        if str(caseinfo["phonenumber"]) != "nan":
            sl.input_phone_num_by_value(str(int(caseinfo["phonenumber"])))
        sl.select_by_value(str(caseinfo["status"]))
        sl.click_search()
        # sl.click_edit()
