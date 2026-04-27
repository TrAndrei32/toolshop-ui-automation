class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.proceed_buttons = {
            1: "[data-test=\"proceed-1\"]",
            2: "[data-test=\"proceed-2\"]",
            3: "[data-test=\"proceed-3\"]",
        }
        self.billing_address = "h3:has-text('Billing Address')"
        self.product_title = "[data-test=\"product-title\"]"
        self.already_logged = "p:has-text('already logged in')"
        self.postal_code = "#postal_code"
        self.house_number = "#house_number"
        self.payment_method = "#payment-method"
        self.finish = "[data-test=\"finish\"]"
        self.payment_successful = "[data-test=\"payment-success-message\"]"

    def check_product_is_in_cart(self):
        self.page.locator(self.product_title).wait_for(state="visible")

    def proceed_to_checkout(self, step: int):
        locator = self.page.locator(self.proceed_buttons[step])
        locator.wait_for(state="visible")
        locator.click()

    def check_you_are_logged(self):
        return self.page.locator(self.already_logged).text_content()

    def check_for_billing_address(self):
        self.page.locator(self.billing_address).wait_for(state="visible")

    def fill_postal_code_house_number(self, postal_code, house_number):
        self.page.fill(self.postal_code, postal_code)
        self.page.fill(self.house_number, house_number)

    def choose_payment_method(self):
        self.page.select_option(self.payment_method, value="cash-on-delivery")
        self.page.locator(self.finish).click()

    def finish_order(self):
        return self.page.locator(self.payment_successful).inner_text()
