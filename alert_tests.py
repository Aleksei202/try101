from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
import time
from BrainBucket.webelements.alerts import Alerts
from BrainBucket.webelements.iframe import IFrame

URL = "http://techskillacademy.net/practice/"


def test_simple_alert():
    browser = Browser(URL)
    alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()']")
    alert_btn.click()

    practice_alerts = Alerts(browser)
    practice_alerts.simple_alert()

    browser.shutdown()


def test_confirmation_alert():
    browser = Browser(URL)
    confirm_btn = Element(browser, By.XPATH, "//button[@onclick='openConfirmationAlert()']")
    confirm_btn.click()

    practice_alerts = Alerts(browser)
    practice_alerts.confirmation_alert_cancel()

    msg = Element(browser, By.ID, 'msg')
    assert msg.get_text() == "You pressed CANCEL!"

    confirm_btn.click()
    practice_alerts.confirmation_alert_ok()

    assert msg.get_text() == "You pressed OK!"

    browser.shutdown()


def test_prompt_alert():
    browser = Browser(URL)
    prompt_btn = Element(browser, By.XPATH, "//button[@onclick='openPrompt()']")

    prompt_btn.click()

    practice_prompt_alert = Alerts(browser)
    text = 'Svetlana'
    practice_prompt_alert.prompt_alert(text)

    msg = "Hello {}! How are you today?".format(text)
    prompt_msg = Element(browser, By.ID, 'demo')
    assert prompt_msg.get_text() == msg

    browser.shutdown()


def test_iframe():
    browser = Browser(URL)
    iframe = Element(browser, By.TAG_NAME, 'iframe')
    practice_iframe = IFrame(browser)
    practice_iframe.switch_to_iframe(iframe)

    time.sleep(2)
    Element(browser, By.XPATH, "//*[@class='logo__title']").wait_until_visible()

    practice_iframe.switch_to_default_content()
    browser.shutdown()


if __name__ == "__main__":
    test_simple_alert()
    test_confirmation_alert()
    test_prompt_alert()
    test_iframe()
