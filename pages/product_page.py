class ProductPage:
    def __init__(self, page):
        self.page = page
        self.cart_button = "[data-test=\"product-name\"]"
        self.cart_icon = "[data-test=\"cart-quantity\"]"
        self.add_cart_button = "#btn-add-to-cart"
        self.open_cart = "[data-test=\"nav-cart\"]"

    def cart_available(self):
        self.page.locator(self.cart_button).wait_for(state="visible")

    def cart_badge(self):
        self.page.locator(self.cart_icon).wait_for(state="visible")

    def add_to_cart(self):
        self.page.locator(self.add_cart_button).click()

    def click_on_cart(self):
        self.page.locator(self.open_cart).click()
        self.page.wait_for_url("**/checkout")
