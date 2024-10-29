import pytest
import allure

from playwright.sync_api import Page,expect,sync_playwright

@pytest.fixture()
def setUp():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page
    yield page
    page.close()
    context.close()
@pytest.mark.negative()
def test_mini_project_negative(setUp):

    page = setUp
    page.goto("https://app.vwo.com/#/login")
    page.wait_for_load_state("networkidle")
    page.locator("//input[@id='login-username']").fill("admin")
    page.locator("//input[@id='login-password']").fill("admin")
    page.locator("//button[@id='js-login-btn']").click()
    error_message_selc = "//div[@id='js-notification-box-msg']"
    page.wait_for_selector(error_message_selc)
    error_msg = page.locator(error_message_selc)
    assert error_msg.text_content() == "Your email, password, IP address or location did not match"


def test_mini_project_positive(setUp):
    page = setUp
    page.goto("https://app.vwo.com/#/login")
    page.wait_for_load_state("networkidle")
    page.locator("//input[@id='login-username']").fill("admin")
    page.locator("//input[@id='login-password']").fill("admin")
    page.locator("//button[@id='js-login-btn']").click()
    error_message_selc = "//div[@id='js-notification-box-msg']"
    page.wait_for_selector(error_message_selc)
    error_msg = page.locator(error_message_selc)
    assert error_msg.text_content() == "Your email, password, IP address or location did not match"
