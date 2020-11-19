from page.main_page import MainPage


class TestTrade:
    def setup_class(self):
        self.main_page = MainPage()

    def test_market_a_open(self):
        self.main_page.trade_page().market_a_open()
