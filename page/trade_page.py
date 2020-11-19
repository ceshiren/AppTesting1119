from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class TradePage(BasePage):
    def market_a_open(self):
        # webview自动化测试可以使用native定位
        self.find(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
