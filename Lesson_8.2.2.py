import time

from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Aleksei ThinkPad\PycharmProjects\chromedriver.exe")

driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")
driver.maximize_window()  # maximizing the browser window
# implicit wait
driver.implicitly_wait(5)
wd_wait = WebDriverWait(driver, 10)

# activating My Account dropdown
account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()

# Selecting Resgister from dropdown
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")))

register_option = driver.find_element_by_xpath("//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
register_option.click()

# 'Register Account' 'explicit wait location
register_account = wd_wait.until(
    EC.visibility_of_element_located((By.ID, "content")))

time.sleep(3)

######
# activating My Account dropdown
account_btn = driver.find_element_by_xpath("//a[@title='My Account']")
account_btn.click()

# Selecting Login from dropdown
wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")))

login_option = driver.find_element_by_xpath("//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
login_option.click()

# 'Returning customer' explicit wait location
returning_customer = wd_wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div/h2')))

time.sleep(3)
driver.quit()
