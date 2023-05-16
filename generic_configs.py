import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture(scope="class")
def init_driver(request):

    supported_browser=["chrome","ch","headlesschrome","firefox","ff"]
    browser=os.environ.get("BROWSER",None)

    if not browser:
        raise Exception("The Environmental variable browser must be set")

    browser=browser.lower()

    if browser not in supported_browser:
        raise Exception(f"The provider browser '{browser}' is not one of the supported browser"
                        f"supported browsers are '{supported_browser}' ")

    if browser in ("chrome","ch"):
        se = Service(executable_path="/chromedriver_mac64/chromedriver")
        driver = webdriver.Chrome(service=se)

    elif browser in ("firefox","ff"):
        pass

    request.cls.driver =driver
    yield
    time.sleep(2)
    driver.quit()


