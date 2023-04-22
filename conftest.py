import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import allure
from allure_commons.types import AttachmentType


@pytest.fixture()
def browser_chrome():
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    # browser.maximize_window()
    yield browser
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    browser.quit()


# @pytest.fixtrue()
# def browser_firefox():
#     service = Service(GeckoDriverManager().install())
#     browser = webdriver.Friefox(service=service)
#     yield browser
#     browser.quit()
