import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoketest
def test_alhymrec_navigation_test_env(browser_chrome):
    browser_chrome.get("https://fyl.vqr.mybluehost.me/")
    page_title = WebDriverWait(browser_chrome, 10).until(EC.title_contains("Homepage"))
    assert "Homepage" in browser_chrome.title
    assert "https://fyl.vqr.mybluehost.me" in browser_chrome.current_url
