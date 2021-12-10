from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.color import Color

from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element
from BrainBucket.pages.home_page import HomePage

from BrainBucket.webelements.actions import Actions
from selenium.webdriver.common.keys import Keys

URL = 'https://techskillacademy.net/brainbucket/index.php?route=common/home'

browser = Browser(URL)
driver = browser.get_driver()

homepage1 = HomePage(browser)

# check PC quantity not 0
homepage1.show_pcs()
pc_btn = Element(browser, By.XPATH, '//*[@id="column-left"]/div[1]/a[2]')
print(pc_btn.get_text())
if pc_btn.get_text() == '   - PC (0)':
    Element(browser, By.XPATH, "//p[contains(text(), 'There are no products')]").wait_until_visible()

# check Mac quantity = 1
homepage2 = HomePage(browser)
homepage2.show_mac_desktops()
mac_btn = Element(browser, By.XPATH, '//*[@id="column-left"]/div[1]/a[3]')
print(mac_btn.get_text())
assert mac_btn.get_text() == '   - Mac (1)'

# check All Desktops open page
homepage3 = HomePage(browser)
homepage3.show_all_desktops()
Element(browser, By.XPATH, '//*[@id="content"]/h2').wait_until_visible()

time.sleep(3)
driver.quit()
