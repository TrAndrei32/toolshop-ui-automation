class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.categories_button = "[data-test=\"nav-categories\"]"
        self.dropdown_handtools = "[data-test=\"nav-hand-tools\"]"
        self.handtools_list = ".col-md-9"
        self.dropdown = "#menu"
        self.sign_out = "[data-test=\"nav-sign-out\"]"

    def categories(self):
        self.page.locator(self.categories_button).click()
        self.page.locator(self.dropdown_handtools).click()

    def products_list(self):
        self.page.locator(self.handtools_list).wait_for(state="visible")

    def log_out(self):
        self.page.locator(self.dropdown).wait_for(state="visible")
        self.page.locator(self.dropdown).click()
        self.page.locator(self.sign_out).wait_for(state="visible")
        self.page.locator(self.sign_out).click()
