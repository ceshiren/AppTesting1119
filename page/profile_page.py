from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By

from page.base_page import BasePage

if TYPE_CHECKING:
    from page.main_page import MainPage

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login_by_password(self, account, password):

        return MainPage()

    def login_by_password_fail(self, account, code):
        self.driver.find_element(By.XPATH, "//*[@text='帐号密码登录']").click()
        self.driver.find_element(By.ID, "login_account").send_keys(account)
        self.driver.find_element(By.ID, "login_password").send_keys(code)
        self.driver.find_element(By.ID, "button_next").click()
        msg = self.driver.find_element(By.ID, "md_content").text

        return self

    def login_by_verify_code_fail(self, account, password):
        self.driver.find_element(By.ID, "tv_login_phone").click()
        self.driver.find_element(By.ID, "register_phone_number").send_keys(account)
        self.driver.find_element(By.ID, "register_code").send_keys(password)
        self.driver.find_element(By.ID, "button_next").click()
        msg = self.driver.find_element(By.ID, "md_content").text
        return msg

    def login_by_verify_code(self, account, code):
        return MainPage()

    def 最近阅读(self):
        pass
