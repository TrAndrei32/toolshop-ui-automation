class HomePage:
    def __init__(self, page):
        self.page = page
        self.signin_button = "[data-test=\"nav-sign-in\"]"

    def signin(self):
        self.page.locator(self.signin_button).wait_for(state="visible")
        self.page.locator(self.signin_button).click()
        self.page.wait_for_url("**/auth/login")
