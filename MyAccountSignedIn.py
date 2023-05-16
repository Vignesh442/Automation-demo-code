
from venv_py_sel.ssqatest.src.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocator
from venv_py_sel.ssqatest.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocator):

    def __init__(self,driver):
        self.driver= driver
        self.sl=SeleniumExtended(self.driver)

    def verify_user_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV__LOGOUT_BTN)
