import pytest
from pages.home_page import HomePage


class TestHomepage:
    @pytest.mark.smoke
    def test_signin_button(self, page, base_url):
        page.goto(base_url)
        signin_button = HomePage(page)
        signin_button.signin()
        assert page.url.endswith("/auth/login")
