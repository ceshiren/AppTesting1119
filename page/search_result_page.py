from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class SearchResultPage(BasePage):
    def get_name(self):
        return self.driver.find_element(MobileBy.ID, "stockName").text

    def cancel(self):
        self.driver.find_element_by_id("action_close").click()
