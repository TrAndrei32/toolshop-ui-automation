class HomePage:
    def __init__(self, page):
        self.page = page
        self.signin_button = "[data-test=\"nav-sign-in\"]"

    def signin(self):
        self.page.click(self.signin_button)
        self.page.wait_for_url("**/auth/login")
