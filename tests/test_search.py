import pytest

from page.main_page import MainPage


class TestSearch:
    def setup_class(self):
        self.main_page = MainPage()

    def test_search(self):
        main_page = MainPage()
        search_page = main_page.search_page()
        search_result_page = search_page.search('pdd')
        assert search_result_page.get_name() == '拼多多'

    @pytest.mark.parametrize("keyword,name", [
        ["pdd", "拼多多"],
        ["alibaba", "阿里巴巴"],
        ["jd", "京东"]
    ])
    def test_search2(self, keyword, name):
        self.result_page = self.main_page.search_page().search(keyword)
        assert self.result_page.get_name() == name

    def teardown(self):
        self.result_page.cancel()
