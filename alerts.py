
import time


class Alerts:
    def __init__(self, browser):
        self.browser = browser

    def simple_alert(self):
        alert = self.browser.get_driver().switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)

    def confirmation_alert_cancel(self):
        alert = self.browser.get_driver().switch_to.alert
        time.sleep(2)
        alert.dismiss()
        time.sleep(2)

    def confirmation_alert_ok(self):
        alert = self.browser.get_driver().switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)

    def prompt_alert(self, text):
        alert = self.browser.get_driver().switch_to.alert
        time.sleep(2)

        alert.send_keys(text)
        alert.accept()
        time.sleep(2)


