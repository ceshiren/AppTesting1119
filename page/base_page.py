from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver=None):
        self.driver: WebDriver = driver

    def quit(self):
        self.driver.quit()

    # 异常处理，使用装饰器为通用函数提供异常捕获
    def find(self, *args):
        try:
            if len(args) == 1:
                return self.driver.find_element(*args)
            else:
                return self.driver.find_element(args[0], args[1])
        except:
            # todo: 异常处理 各种异常弹框 截屏 开始录像
            self.find(*args)

    def click(self, locator):
        self.find(locator).click()

    def send_keys(self, text, locator):
        self.find(locator).send_keys(text)
