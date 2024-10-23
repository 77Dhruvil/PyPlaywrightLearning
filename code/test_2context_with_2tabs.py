import pytest
import allure

from playwright.sync_api import Page,expect,sync_playwright

def test_2context_with_2tabs():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    context1 = browser.new_context()
    page = context.new_page()
    page2 = context1.new_page()
    page.goto("https://flipkart.com")
    page2.goto("https://amazon.com")

    context.close()