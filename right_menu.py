from BrainBucket.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class RightMenu:
    def __init__(self, browser):
        self.login_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[1]")
        self.registration_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[2]")
        self.forgotten_password_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[3]")
        self.my_account_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[4]")
        #AN my code start
        self.address_book_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[5]")
        self.wish_list_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[6]")
        self.order_history_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[7]")
        self.downloads_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[8]")
        self.recurring_payments_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[9]")
        self.reward_points_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[10]")
        self.returns_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[11]")
        self.transactions_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[12]")
        self.newsletter_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[13]")
        #AN code end

    def click_login(self):
        self.login_btn.click()

    def click_registration(self):
        self.registration_btn.click()

    def click_forgotten_btn(self):
        self.forgotten_password_btn.click()

    def click_my_account(self):
        self.my_account_btn.click()

    #AN code start 12-01-21
    def click_address_book(self):
        self.address_book_btn.click()

    def click_wish_list(self):
        self.wish_list_btn.click()

    def click_order_history(self):
        self.order_history_btn.click()

    def click_downloads(self):
        self.downloads_btn.click()

    def click_recurring_payments(self):
        self.recurring_payments_btn.click()

    def click_reward_points(self):
        self.reward_points_btn.click()

    def click_returns(self):
        self.returns_btn.click()

    def click_transactions(self):
        self.transactions_btn.click()

    def click_newsletter(self):
        self.newsletter_btn.click()
    #AN code end


