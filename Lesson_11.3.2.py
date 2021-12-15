from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *

from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element
from datetime import datetime


URL = 'https://techskillacademy.net/brainbucket/index.php?route=common/home'

browser = Browser(URL)
driver = browser.get_driver()

file = datetime.now()
print(file)
file_name = "../screenshots/" + file.strftime("%d%m%Y_%H%M%S.png")
print(file_name)

try:
    logo_banner = Element(browser, By.XPATH, '//*[@id="logo"]/a2/img').wait_until_visible()
except TimeoutException:
    print('XPATH does not found')
    browser.save_screenshot()

time.sleep(3)
driver.quit()
