import pytest
from pages.dashboard_page import DashboardPage


class TestDashboard:
    @pytest.mark.smoke
    def test_categories_list(self, logged_in_page):
        dashboard_page = DashboardPage(logged_in_page)
        dashboard_page.categories()
        assert logged_in_page.url.endswith("/category/hand-tools")
        logged_in_page.locator("[data-test^='product-']").first.wait_for(state="visible")
        assert logged_in_page.locator("[data-test^='product-']").count() > 0

    @pytest.mark.smoke
    def test_logout(self, logged_in_page):
        dashboard_page = DashboardPage(logged_in_page)
        dashboard_page.log_out()
        logged_in_page.wait_for_url("**/auth/login")
        assert logged_in_page.locator(
            "#email").is_visible()
