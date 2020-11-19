from page.base_page import BasePage
from page.search_result_page import SearchResultPage


class SearchPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()

        return SearchResultPage(self.driver)
