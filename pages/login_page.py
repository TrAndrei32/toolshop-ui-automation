class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email = "#email"
        self.password = "#password"
        self.login_button = ".btnSubmit"
        self.name_menu = "[data-test=\"nav-menu\"]"
        self.error_message = ".help-block"

    def login(self, email, password):
        self.page.fill(self.email, email)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)

    def wait_for_login_success(self):
        self.page.locator(self.name_menu).wait_for(state="visible")

    def name(self):
        self.page.locator(self.name_menu).wait_for(state="visible")
        return self.page.locator(self.name_menu).inner_text()

    def get_error_message(self):
        return self.page.locator(self.error_message).text_content()
