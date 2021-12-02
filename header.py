import time

from BrainBucket.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class Header:
    def __init__(self, browser):
        self.my_account_btn = Element(browser, By.XPATH, "//a[@title='My Account']")
        self.my_acccount_dropdown = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")
        self.register_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
        self.login_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
        self.wish_list_btn = Element(browser, By.ID, "wishlist-total")
        self.shopping_list_btn = Element(browser, By.XPATH, "//a[@title='Shopping Cart']")
        self.checkout_btn = Element(browser, By.XPATH, "//a[@title='Checkout']")
        self.currency_btn = Element(browser, By.ID, "form-currency")
        # AN code 12-01-21 start
        self.currency_btn_dropdown = Element(browser, By.XPATH, "//*[@class='dropdown-menu']")
        self.currency_btn_dropdown_eur = Element(browser, By.XPATH,
                                                 "//*[@class='dropdown-menu']/li[1]")
        self.currency_btn_dropdown_gbr = Element(browser, By.XPATH,
                                                 "//*[@class='dropdown-menu']/li[2]")
        self.currency_btn_dropdown_usd = Element(browser, By.XPATH,
                                                 "//*[@class='dropdown-menu']/li[3]")
        # AN code 12-01-21 end
        self.logo = Element(browser, By.ID, "logo")
        self.search = Element(browser, By.XPATH, "//input[@type='text']")
        # AN code 12-01-21 start
        self.search_btn = Element(browser, By.XPATH, "//*[@class='btn btn-default btn-lg']")
        # AN code 12-01-21 end

    def verify_logo_is_visible(self):
        return self.logo.wait_until_visible()

    def open_registration_form(self):
        self.my_account_btn.click()
        self.my_acccount_dropdown.wait_until_visible()
        self.register_btn.click()

    def open_login_page(self):
        self.my_account_btn.click()
        self.my_acccount_dropdown.wait_until_visible()
        self.login_btn.click()

    def change_currency(self, new_currency):
        # AN code 12-01-21
        self.currency_btn.click()
        self.currency_btn_dropdown.wait_until_visible()
        currency = new_currency.lower()
        if currency == 'eur':
            self.currency_btn_dropdown_eur.click()

        elif currency == 'gbr':
            self.currency_btn_dropdown_gbr.click()
        elif currency == 'usd':
            self.currency_btn_dropdown_usd.click()

    def open_wishlist(self):
        # AN code 12-01-21
        self.wish_list_btn.click()

    def search_for(self, text):
        # AN code 12-01-21
        self.search.enter_text(text)
        time.sleep(3)
        self.search_btn.click()
