
import time


class IFrame:
    def __init__(self, browser):
        self.browser = browser

    def switch_to_iframe(self, iframe):
        self.browser.get_driver().switch_to.frame(iframe.get_element())
        time.sleep(2)

    def switch_to_default_content(self):
        self.browser.get_driver().switch_to.default_content()
        time.sleep(2)

