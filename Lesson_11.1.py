
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.color import Color

from BrainBucket.webelements.browser import Browser
from BrainBucket.webelements.UIElement import UIElement as Element

from BrainBucket.webelements.action_chains import Actions
from selenium.webdriver.common.keys import Keys

URL = 'https://techskillacademy.net/practice/'

browser = Browser(URL)
driver = browser.get_driver()
techskillacademy = Actions(browser)

double_click_btn = Element(browser, By.XPATH, '//*[@id="card"]')
keydown_btn = Element(browser, By.XPATH, '//*[@id="key_practice"]/input')
context_menu_btn = Element(browser, By.XPATH, '//*[@id="context_menu"]')
drag_and_drop_btn = Element(browser, By.XPATH, '//*[@id="droplogo123"]')
logo_pic = Element(browser, By.XPATH, '//*[@id="drag1"]')

# Double click checking
techskillacademy.double_click(double_click_btn)

backround_color = double_click_btn.value_of_css_property("background-color")
print(backround_color)
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(255, 179, 128)'

# Keydown checking
keydown_btn.click()
techskillacademy.send_keys_to_element(keydown_btn, Keys.ENTER)
#keydown_btn.enter_text(Keys.ENTER)
hidden_text = Element(browser, By.XPATH, "//p[text() ='You pressed the key!']").wait_until_visible()

# Right click context menu checking
# change color check
techskillacademy.right_click(context_menu_btn)
change_color_btn = Element(browser, By.XPATH, "//*[@class='menu-options']/li[1]")
change_color_btn.click()

backround_color = context_menu_btn.value_of_css_property("background-color")
print(backround_color)
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(204, 255, 245)'


time.sleep(2)

# change font
techskillacademy.right_click(context_menu_btn)
change_font_btn = Element(browser, By.XPATH, "//*[@class='menu-options']/li[2]")
change_font_btn.click()
techskillacademy.key_down(Keys.ESCAPE)

text_font = context_menu_btn.value_of_css_property("font-weight")
print(text_font)
assert text_font == '700'


# load CleverOnly web page

techskillacademy.right_click(context_menu_btn)
tech_skill_academy_btn = Element(browser, By.XPATH, "//*[@class='menu-options']/li[3]/a")
tech_skill_academy_btn.click()

driver.switch_to.window(driver.window_handles[1])

logo_clever_only = Element(browser, By.XPATH, "//a/div").wait_until_visible()


time.sleep(3)

driver.quit()



