from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver=None):
        self.driver: WebDriver = driver

    def quit(self):
        self.driver.quit()
