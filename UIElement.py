from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement


class UIElement:
    """
    This class is for any web element on the page, takes as parameters browser, method of locating element
    and locator itself
    """

    def __init__(self, browser, by, locator):
        self.driver = browser.get_driver()
        self.wait = browser.get_wd_wait()
        self._by = by
        self._locator = locator

    def get_element(self):
        """
        Locates web element on the page
        :return: WebElement object
        """
        return self.driver.find_element(self._by, self._locator)

    def wait_until_visible(self):
        """
        Waits until web element is visible
        :return: WebElement object
        """
        return self.wait.until(EC.visibility_of_element_located((self._by, self._locator)))

    def get_text(self, wait=True):
        """
        Gets the text of the web element
        :param wait: put False, if you don't want to wait until element will be visible
        :return: text of the WebElement
        """
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()
        return element.text

    def get_attribute(self, attribute, wait=True):
        """
        Returns the attribute of web element (in html it will  be the attrbiute of the tag)
        :param attribute: name of the attribute to return
        :param wait: put False, if you don't want to wait until element will be visible
        :return: value of the attribute specified
        """
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()
        return element.get_attribute(attribute)

    def click(self):
        """
        Waits until element will be clickable and clicks on it
        """
        self.wait.until(EC.element_to_be_clickable((self._by, self._locator))).click()

    def enter_text(self, text, wait=False):
        """
        Sends keys to the input field
        :param text: text to type in
        :param wait: put True, if you want to wait until element will be visible
        """
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()

        element.clear()
        element.send_keys(text)

    def submit(self):
        """
        Clicks on submit button of the form
        """
        self.wait.until(EC.element_to_be_clickable((self._by, self._locator))).submit()

    def send_keys(self, text):

        pass

    # AN my code
    def value_of_css_property(self, param):
        element = self.get_element()
        return element.value_of_css_property(param)

    '''def element_is_displayed(self):
        element = self.get_element()
        return element.is_displayed()'''
