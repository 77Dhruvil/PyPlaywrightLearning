import time

import pytest
import allure

from playwright.sync_api import Page,expect,sync_playwright

def test_locators1_fovero():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context =  browser.new_context()
    page = browser.new_page()
    page.goto("https://awesomeqa.com/pw/locators1.html")
    page.wait_for_load_state("networkidle")
    page.get_by_label("subscribe").check()
    page.get_by_role("button",name="Submit").click()


    expect(page.get_by_role("listitem")).to_have_count(5)
    for row in page.get_by_role("listitem").all():
        print(row.text_content())

    time.sleep(10)