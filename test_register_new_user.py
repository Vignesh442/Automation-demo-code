

import pytest

from venv_py_sel.ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from venv_py_sel.ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from venv_py_sel.ssqatest.src.helpers.generic_helpers import generate_random_email_and_password

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        # go to my account first open the url
        my_account_o=MyAccountSignedOut(self.driver) # always pass the driver path
        my_account_i=MyAccountSignedIn(self.driver)
        my_account_o.go_to_my_account()
        #fill the email address in email locator
        rand_email=generate_random_email_and_password()
        my_account_o.input_register_email(rand_email["email"])
        #fill the password in password locator
        my_account_o.input_register_password("Password@1234!!")
        # Click the Register Button
        my_account_o.click_register_button()
        #verify user is registered
        my_account_i.verify_user_signed_in()


