from typing import TYPE_CHECKING

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.search_page import SearchPage
from page.profile_page import ProfilePage
from page.trade_page import TradePage


class MainPage(BasePage):
    #find_element(*self._HOME_SEARCH)
    _HOME_SEARCH = (By.ID, "com.xueqiu.android:id/home_search")

    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["ensureWebviewsHavePages"] = True
        # app入口，通过logcat找到
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 不清理数据，在正常的自动化测试中会保持为False，并配合autoGrantPermissions
        caps["noReset"] = True
        # 中文支持
        caps["unicodeKeyBoard "] = True
        caps["resetKeyBoard "] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 增加隐式等待
        self.driver.implicitly_wait(10)

        # 增加显式等待判断app是否完整启动
        WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(self._HOME_SEARCH)
        )

    def search_page(self):
        self.driver.find_element(*self._HOME_SEARCH).click()
        return SearchPage(self.driver)

    def profile_page(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='我的' and contains(@resource-id, 'tab_name')]").click()

        return ProfilePage(self.driver)

    def trade_page(self):
        self.find(By.XPATH, "//*[@text='交易']").click()
        return TradePage(self.driver)
