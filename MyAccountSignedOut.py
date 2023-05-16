
from venv_py_sel.ssqatest.src.pages.locators.MyAccountSignedoutLocator import MyAccountSignedoutLocator
from venv_py_sel.ssqatest.src.SeleniumExtended import SeleniumExtended
#from venv_py_sel.ssqatest.src.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedoutLocator):

    endpoint='/my-account/'

    def __init__(self,driver):
        self.driver =driver
        self.sl=SeleniumExtended(self.driver)

    def go_to_my_account(self):
        url='http://demostore.supersqa.com/'
        my_account_url=url+self.endpoint
        self.driver.get(my_account_url)
        self.driver.maximize_window()
        logger.info(f"Going to the url ::{my_account_url}")

    def input_login_username(self,username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME,username)

    def input_login_password(self,Password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD,Password)

    def click_login_button(self):
        logger.debug("Clicking the login Button ")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displaced(self,exp_err):

        self.sl.wait_until_element_contains_text(self.ERROR_UL,exp_err)
        print('The displaced err and Expected error are same')

    def input_register_email(self,email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL,email)

    def input_register_password(self,password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD,password)

    def click_register_button(self):
        logger.debug("Clicking the register Button ")
        self.sl.wait_and_click(self.REGISTER_BTN)
