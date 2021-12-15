from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from datetime import datetime


class Browser:
    """
    This class is wrapper around Selenium driver
    """

    def __init__(self, url, browser_name=""):
        # decide which browser to open, can be extended
        if browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox(executable_path='drivers/geckodriver')
        else:
            #AN my code start Lesson 11.3.1
            try:
                self.chrome_path = r"C:\Users\Aleksei ThinkPad\PycharmProjects\chromedriver.exe"
                self.driver = webdriver.Chrome(executable_path=self.chrome_path)
            except WebDriverException:
                print("Webdriver path wrong", self.chrome_path)
            #AN my code end

            self.driver.get(url)

        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # by default 10, but we can add this like a parameter

    def save_screenshot(self):
        now = datetime.now()
        filename = "./screenshots/" + now.strftime("%d%m%Y_%H%M%S.png")
        self.driver.save_screenshot(filename)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()
