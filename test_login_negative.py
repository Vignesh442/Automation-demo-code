import pytest
from venv_py_sel.ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("init_driver")

class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):

        my_account =MyAccountSignedOut(self.driver)
        # go to my account
        my_account.go_to_my_account()
        # type username
        my_account.input_login_username("vignesh")
        # type password
        my_account.input_login_password("12345")
        # click login
        my_account.click_login_button()
        # verify the error message
        expected_err='Error: The password you entered for the username Vignesh is incorrect. Lost your password?'
        my_account.wait_until_error_is_displaced(expected_err)
