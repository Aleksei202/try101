from BrainBucket.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class Footer:
    def __init__(self, browser):
        self.about_us_btn = Element(browser, By.XPATH, "//*[text()='About Us']")
        self.delivery_information_btn = Element(browser, By.XPATH, "//*[text()='Delivery Information']")
        self.privacy_policy_btn = Element(browser, By.XPATH, "//*[text()='Privacy Policy']")
        self.terms_and_conditions_btn = Element(browser, By.XPATH, "//*[text()='Terms & Conditions']")

        self.contact_us_btn = Element(browser, By.XPATH, "//*[text()='Contact Us']")
        self.returns_btn = Element(browser, By.XPATH, "(//*[text()='Returns'])[2]")
        self.site_map_btn = Element(browser, By.XPATH, "//*[text()='Site Map']")

        self.brands_btn = Element(browser, By.XPATH, "//*[text()='Brands']")
        self.gift_certificates_btn = Element(browser, By.XPATH, "//*[text()='Gift Certificates']")
        self.affiliates_btn = Element(browser, By.XPATH, "//*[text()='Affiliates']")
        self.specials_btn = Element(browser, By.XPATH, "//*[text()='Specials']")

        self.my_account_btn = Element(browser, By.XPATH, "(//*[text()='My Account'])[3]")
        self.order_history_btn = Element(browser, By.XPATH, "//*[text()='Order History']")
        self.wish_list_btn = Element(browser, By.XPATH, "(//*[text()='Wish List'])[2]")
        self.newsletter_btn = Element(browser, By.XPATH, "//*[text()='Newsletter']")





