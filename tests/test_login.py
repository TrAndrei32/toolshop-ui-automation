import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import os


class TestLogin:
    @pytest.mark.smoke
    def test_login_valid(self, page, base_url):
        page.goto(base_url, wait_until="networkidle")
        home_page = HomePage(page)
        home_page.signin()
        login_page = LoginPage(page)
        login_page.login(os.getenv("EMAIL"),
                         os.getenv("PASSWORD"))
        menu_name = login_page.name()
        assert "John Doe" in menu_name

    @pytest.mark.smoke
    def test_login_invalid(self, page, base_url):
        page.goto(base_url, wait_until="networkidle")
        home_page = HomePage(page)
        home_page.signin()
        login_page = LoginPage(page)
        login_page.login(os.getenv("EMAIL"), "password")
        error = login_page.get_error_message()
        assert "Invalid email or password" in error
