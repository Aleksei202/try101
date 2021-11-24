from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Aleksei ThinkPad\PycharmProjects\chromedriver.exe")
# to start Firefox use the line below
# driver = webdriver.Firefox(executable_path='drivers/geckodriver')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")

driver.maximize_window()  # maximizing the browser window

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

# new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")


# updated new_registration_btn with WebDriverWait method

wd_wait = WebDriverWait(driver, 10)
new_registrant_btn = wd_wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))

# my code Aleksei Nevzorov 11-10-2021
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("12345")

login_btn = driver.find_element_by_xpath("//a[contains(text(), 'Login')]")

# login_btn.click()


# getting the background color of the button
backround_color = new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'

new_registrant_btn.click()

# Register Account
# Personal Details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

# my code Aleksei Nevzorov 11-10-2021
email_field = driver.find_element_by_xpath("//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class

telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

# web elements in""" """ does not pass assert for class attribute
"""fax_field = driver.find_element_by_xpath("//fieldset/div[6]")
fax_field_class = fax_field.get_attribute("class")
assert "required" in fax_field_class

company_field = driver.find_element_by_xpath("//fieldset[2]/div[1]")
company_field_class = company_field.get_attribute("class")
assert "required" in company_field_class"""

address_1_field = driver.find_element_by_xpath("//fieldset[2]/div[2]")
address_1_field_class = address_1_field.get_attribute("class")
assert "required" in address_1_field_class

"""address_2_field = driver.find_element_by_xpath("//fieldset[2]/div[3]")
address_2_field_class = address_2_field.get_attribute("class")
assert "required" in address_2_field_class"""

city_field = driver.find_element_by_xpath("//fieldset[2]/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class

"""post_code_field = driver.find_element_by_xpath("//fieldset[2]/div[5]")
post_code_field_class = city_field.get_attribute("class")
assert "required" in post_code_field_class"""

password_field = driver.find_element_by_xpath("//fieldset[3]/div[1]")
password_field_class = city_field.get_attribute("class")
assert "required" in password_field_class

password_confirm_field = driver.find_element_by_xpath("//fieldset[3]/div[2]")
password_confirm_field_class = password_confirm_field.get_attribute("class")
assert "required" in password_confirm_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Aleksei")

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Nevzorov")

email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("wrewqer@rwer.com")

telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("23432142142")

fax_input = driver.find_element_by_id("input-fax")
fax_input.clear()
fax_input.send_keys("23432142142")

company_input = driver.find_element_by_id("input-company")
company_input.clear()
company_input.send_keys("GEMINI")

address_1_input = driver.find_element_by_id("input-address-1")
address_1_input.clear()
address_1_input.send_keys("WoodHill")

address_2_input = driver.find_element_by_id("input-address-2")
address_2_input.clear()
address_2_input.send_keys("Gibsonia")

city_input = driver.find_element_by_id("input-city")
city_input.clear()
city_input.send_keys("Pittsburgh")

postcode_input = driver.find_element_by_id("input-postcode")
postcode_input.clear()
postcode_input.send_keys("123789")

# select country
country_dropdown = driver.find_element_by_id("input-country")
country_dropdown_select = Select(country_dropdown)
country_dropdown_select.select_by_value("34")

# agree to privacy policy
privacy_policy_btn = driver.find_element_by_xpath("//input[@name='agree' and @value='1']")
if not privacy_policy_btn.is_selected():
    privacy_policy_btn.click()

time.sleep(2)

# unsubscribe to newsletter
subscribe_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='0']")
if not subscribe_btn.is_selected():
    subscribe_btn.click()

time.sleep(2)

password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("strongpassword")

confirm_input = driver.find_element_by_id("input-confirm")
confirm_input.clear()
confirm_input.send_keys("strongpassword")

continue_btn = driver.find_element_by_xpath("//*/form/div/div/input[2]")
backround_color = continue_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'

driver.quit()
