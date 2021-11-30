from BrainBucket.UIElement import UIElement as Element


class RadiobuttonCheckbox(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def checkbox(self):
        checkbox_btn = self.get_element()
        if not checkbox_btn.is_selected():
            checkbox_btn.click()
