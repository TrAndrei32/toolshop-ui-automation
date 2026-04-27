import pytest
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="function")
def logged_in_page(page):
    from pages.home_page import HomePage
    from pages.login_page import LoginPage
    page.goto(BASE_URL)
    home_page = HomePage(page)
    home_page.signin()
    login_page = LoginPage(page)
    login_page.login(os.getenv("EMAIL"),
                     os.getenv("PASSWORD"))
    login_page.wait_for_login_success()
    return page


@pytest.fixture(scope="function")
def product_added_to_cart(logged_in_page):
    from pages.dashboard_page import DashboardPage
    from pages.handtools_page import HandTools
    from pages.product_page import ProductPage
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.categories()
    handtools = HandTools(logged_in_page)
    handtools.product()
    product_page = ProductPage(logged_in_page)
    product_page.cart_available()
    product_page.add_to_cart()
    product_page.click_on_cart()
    return logged_in_page
