import logging
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    logger = logging.getLogger(__name__)

    # 创建一个init方法用于把driver传进来
    def __init__(self, d):
        self.driver = d

    # 定位一个元素
    def find_ele(self, xpath) -> "WebElement":
        try:
            self.driver.implicitly_wait(10)
            ele = self.driver.find_element(By.XPATH, xpath)
            self.logger.info("元素定位成功："+ xpath + "")
            return ele
        except Exception:
            self.logger.error("元素定位失败：" + xpath)
            #错误截图
            error_img_path = "./files/" + str(int(time.time())) + ".png"
            self.driver.save_screenshot(error_img_path)
            with open(error_img_path, "rb") as f:
                stream = f.read()
                allure.attach(body=stream, name=error_img_path, attachment_type=allure.attachment_type.PNG)
            raise

    # 定位多个元素
    def find_eles(self, xpath):
        self.driver.implicitly_wait(10)
        return self.driver.find_elements(By.XPATH, xpath)

    # 调整框架
    def goto_frame(self, xpath1, xpath2):  # ,xpath3=None,xpath4=None
        # 点击第一级列表
        self.find_ele(xpath1).click()

        # 点击第二级列表
        self.find_ele(xpath2).click()

        # # 点击第三级列表
        # if xpath3 is not None:
        #     self.find_ele(xpath3).click()

        # # 点击第四级列表
        # if xpath4 is not None:
        #     self.find_ele(xpath4).click()

        # 进入框架
        self.driver.switch_to.frame("iframe3")
