import pytest
from pages.dashboard_page import DashboardPage
from pages.handtools_page import HandTools
from pages.product_page import ProductPage


class TestProduct:
    @pytest.mark.smoke
    def test_add_product_to_cart(self, logged_in_page):
        dashboard_page = DashboardPage(logged_in_page)
        dashboard_page.categories()
        handtools = HandTools(logged_in_page)
        handtools.product()
        product_page = ProductPage(logged_in_page)
        product_page.cart_available()
        product_page.add_to_cart()
        product_page.cart_badge()
        product_page.click_on_cart()
        assert logged_in_page.url.endswith("/checkout")
        logged_in_page.locator("[data-test='product-title']").wait_for(state="visible")
        assert logged_in_page.locator("[data-test='product-title']").is_visible()
