from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BrainBucket.browser import Browser
from BrainBucket.UIElement import UIElement as Element

# instance Browser creation
browser = Browser("https://techskillacademy.net/brainbucket/index.php?route=account/login")
# getting url opning in Chrome
driver = browser.get_driver()

# getting a method .get_wd_wait
browser.get_wd_wait()
#
continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
continue_btn.click()


time.sleep(3)
browser.shutdown()
