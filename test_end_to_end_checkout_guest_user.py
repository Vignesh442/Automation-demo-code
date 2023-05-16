
import pytest
from venv_py_sel.ssqatest.src.pages.HomePage import HomePage
from venv_py_sel.ssqatest.src.pages.Header import Header
from venv_py_sel.ssqatest.src.pages.CartPage import CartPage
from venv_py_sel.ssqatest.src.configs.generic_configs import GenericConfigs
from venv_py_sel.ssqatest.src.pages.CheckoutPage import CheckoutPage
from venv_py_sel.ssqatest.src.pages.OrderReceivedPage import OrderReceivedPage
import time

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        # go the Homepage
        home_p=HomePage(self.driver)
        header=Header(self.driver)
        cart_p=CartPage(self.driver)
        checkout_p=CheckoutPage(self.driver)
        order_received_p=OrderReceivedPage(self.driver)


        home_p.go_to_my_page()
        # add 1 item to cart
        home_p.click_first_add_to_cart_button()
        # make sure the cart is updated before going to cart
        header.wait_untill_cart_item_count(1)
        # go to cart
        header.click_on_cart_on_right_header()
        # get all products names in cart
        product_names=cart_p.get_all_products_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 Item in cart but found {len(product_names)}"
        # apply for free coupon
        coupon_code=GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)
        # Click on Checkout
        cart_p.click_on_proceed_to_checkout()
        # fill in form
        checkout_p.fill_in_billing_info()
        # click On Place order
        checkout_p.click_place_order()
        # verify Order is Received
        order_received_p.verify_order_received_page_loaded()

        # verify Order is recorded in db(Via sql or api)
