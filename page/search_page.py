from page.search_result_page import SearchResultPage


class SearchPage:

    def __init__(self, driver):
        self.driver=driver

    def search(self, keyword):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()

        return SearchResultPage(self.driver)