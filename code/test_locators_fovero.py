import pytest
import allure

from playwright.sync_api import Page,sync_playwright,expect

def test_locators_fovero():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://fovero.app/signin")
    page.wait_for_load_state("networkidle")
    page.locator("#email").fill("dhruvil.patel@concettolabs.com")
    page.locator("#password").fill("Devil@1234")
    page.locator('//html/body/div/div[3]/div/div/div[2]/div/div/form/div[2]/div/button').click()
    page.wait_for_load_state("networkidle")
    #page.locator("#w-100 fs-7 btn btn-primary").click()
    error_message = page.locator('div.Toastify__toast-body > div.Toastify__toast-icon.Toastify--animate-icon.Toastify__zoom-enter')
    expect(error_message).to_have_text('Incorrect username and password.')
    context.close()