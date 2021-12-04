from BrainBucket.header import Header
from BrainBucket.right_menu import RightMenu
from BrainBucket.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
        # AN code start
        self.email_input = Element(browser, By.XPATH, "//*[@id='input-email']")
        self.password_input = Element(browser, By.XPATH, "//*[@id='input-password']")
        self.login_btn = Element(browser, By.XPATH, "//input[@value='Login']")
        # AN code end

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()

    # AN start code
    def input_email(self, text):
        self.email_input.enter_text(text)

    def input_password(self, text):
        self.password_input.enter_text(text)

    def click_login(self):
        self.login_btn.click()
        # AN end code
