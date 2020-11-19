from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.search_page import SearchPage


class MainPage:
    _HOME_SEARCH = "com.xueqiu.android:id/home_search"

    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["ensureWebviewsHavePages"] = True
        # app入口，通过logcat找到
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 不清理数据
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 增加隐式等待
        self.driver.implicitly_wait(10)

        # 增加显式等待判断app是否完整启动
        WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(
                (MobileBy.ID, self._HOME_SEARCH))
        )


    def search_page(self):
        self.driver.find_element_by_id(self._HOME_SEARCH).click()
        return SearchPage(self.driver)