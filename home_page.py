from BrainBucket.components.navigation_bar import NavigationBar
from BrainBucket.components.header import Header


class HomePage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.navbar = NavigationBar(browser)

    def show_all_desktops(self):
        self.navbar.show_all_desktops()

    def show_pcs(self):
        self.navbar.show_pcs()

    def show_mac_desktops(self):
        self.navbar.show_mac_desktops()

    def show_all_laptops(self):
        self.navbar.show_all_laptops()

    def show_windows_laptops(self):
        self.navbar.show_windows_laptops()

    def show_all_components(self):
        self.navbar.show_all_components()

    def show_mice(self):
        self.navbar.show_mice()

    def show_monitors(self):
        self.navbar.show_monitors()

    #AN code start
    def show_scanners(self):
        self.navbar.show_scanners()

    def show_printers(self):
        self.show_printers()

    def show_web_cameras(self):
        self.show_web_cameras()