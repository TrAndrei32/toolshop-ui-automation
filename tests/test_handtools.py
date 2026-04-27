import pytest
from pages.handtools_page import HandTools
from pages.dashboard_page import DashboardPage


class TestHandtools:
    @pytest.mark.smoke
    def test_list_available(self, logged_in_page):
        dashboard_page = DashboardPage(logged_in_page)
        dashboard_page.categories()
        dashboard_page.products_list()

    @pytest.mark.smoke
    def test_add_first_product(self, logged_in_page):
        dashboard_page = DashboardPage(logged_in_page)
        dashboard_page.categories()
        handtools = HandTools(logged_in_page)
        handtools.product()
        all_products = handtools.count_products()
        assert "/product/" in logged_in_page.url
        logged_in_page.locator("[data-test='product-name']").wait_for(state="visible")
        assert logged_in_page.locator("[data-test='product-name']").is_visible()
        print(f"\nAll products: {all_products}")
