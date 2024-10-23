import pytest
import allure
from playwright.sync_api import Page, sync_playwright, expect

def test_2tabs():
    #1 Browser and page
    browser = sync_playwright().start().chromium.launch(headless=False)
    #Create New Incongnito Browser context
    context = browser.new_context()
    page = context.new_page()
    page1 = context.new_page()

    #2. Conde INteraction with the HTML page
    page.goto("https://concettolabs.com")
    page1.goto("https://google.com")

    #3. Validation
    expect(page).to_have_title("Microsoft Power Platform and Mobile App Development Company")

    #dispose context once it is not needed.
    context.close()

