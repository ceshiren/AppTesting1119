# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver

# 测试用例化改造
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 传统型非PO模式的测试用例
class TestDemo:


    # 测试预置装置
    def setup_class(self):
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
            expected_conditions.visibility_of_element_located((MobileBy.ID, self.HOME_SEARCH)))

    @pytest.mark.parametrize("keyword,name", [
        ["pdd", "拼多多"],
        ["alibaba", "阿里巴巴"],
        ["jd", "京东"]
    ])
    def test_demo(self, keyword, name):
        driver = self.driver

        driver.find_element_by_id(self.HOME_SEARCH).click()
        driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        driver.find_element_by_id("com.xueqiu.android:id/name").click()
        # driver.find_element_by_xpath("//*[@text='拼多多']").click()
        # 1.19.0 开始支持css
        # driver.find_element_by_css_selector("[text='拼多多']").click()

        # 断言
        assert driver.find_element(MobileBy.ID, "stockName").text == name
        driver.find_element_by_id("action_close").click()

    def test_demo2(self):
        driver = self.driver

        # driver.find_element(MobileBy.XPATH, "//*[@text='行情' and @resource-id='com.xueqiu.android:id/tab_name']").click()
        driver.find_element(MobileBy.XPATH, "//*[@text='行情' and contains(@resource-id, 'tab_name')]").click()
        assert driver.find_element(By.ID, "single_line_quote_name").text == "上证指数"

    # 当前类中所有测试用例执行完成后再执行这个方法
    def teardown_class(self):
        self.driver.quit()
