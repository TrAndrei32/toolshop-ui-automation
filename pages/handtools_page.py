class HandTools:
    def __init__(self, page):
        self.page = page
        self.card_product = "[data-test^=\"product-\"]"

    def product(self):
        self.page.locator(self.card_product).first.wait_for(state="visible")
        self.page.locator(self.card_product).first.click()

    def count_products(self):
        return self.page.locator(self.card_product).count()
