import pytest
from selenium import webdriver

from poms.login_page import LoginPage


@pytest.fixture(scope="function",autouse=False)
def all_case_fixture():
    print("打开浏览器，登陆")
    driver = login_ruoyi()
    yield driver
    print("关闭浏览器")


def login_ruoyi():
    # 不让浏览器自动关闭
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)

    # 创建浏览器对象
    driver = webdriver.Edge(options=options)

    # 加载项目地址
    driver.get("https://demo.ruoyi.vip/login")

    #登陆
    code = input("请输入验证码：")
    LoginPage(driver).login(code)

    return driver
