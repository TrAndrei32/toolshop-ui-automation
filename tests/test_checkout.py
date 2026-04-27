import pytest
from pages.checkout_page import CheckoutPage
import os


class TestCheckout:
    @pytest.mark.smoke
    def test_proceed_checkout(self, product_added_to_cart):
        checkout_page = CheckoutPage(product_added_to_cart)
        checkout_page.check_product_is_in_cart()
        checkout_page.proceed_to_checkout(1)
        disclaimer = checkout_page.check_you_are_logged()
        assert "already logged in" in disclaimer
        checkout_page.proceed_to_checkout(2)
        checkout_page.check_for_billing_address()
        checkout_page.fill_postal_code_house_number(os.getenv("POSTAL_CODE"),
                                                    os.getenv("HOUSE_NUMBER"))
        checkout_page.proceed_to_checkout(3)
        checkout_page.choose_payment_method()
        message = checkout_page.finish_order()
        assert "Payment was successful" in message
