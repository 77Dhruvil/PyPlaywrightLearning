import pytest
import allure

from playwright.sync_api import Page ,expect, sync_playwright

def test_foverologin():
    #1. Browser and page
    browser = sync_playwright().start().chromium.launch(headless=False)
    page = browser.new_page()

    #2. Code INteraction with the html web page
    page.goto("https://fovero.app/signin")
    breakpoint()

    #3. Validation
    expect(page).to_have_title("Fovero")