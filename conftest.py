import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

@pytest.fixture()
def browser_chrome():
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()

# @pytest.fixtrue()
# def browser_firefox():
#     service = Service(GeckoDriverManager().install())
#     browser = webdriver.Friefox(service=service)
#     yield browser
#     browser.quit()
