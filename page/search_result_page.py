from appium.webdriver.common.mobileby import MobileBy


class SearchResultPage:
    def __init__(self, driver):
        self.driver=driver

    def get_name(self):
        return self.driver.find_element(MobileBy.ID, "stockName").text

    def cancel(self):
        self.driver.find_element_by_id("action_close").click()
