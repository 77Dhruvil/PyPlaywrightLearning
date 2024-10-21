import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://fovero.app/")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("dhruvil.patel@concettolabs.com")
    page.get_by_placeholder("Email").press("Tab")
    page.get_by_placeholder("Password").fill("Devil@123")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Dhruvil Patel").click()
    page.get_by_role("button", name="Logout Logout").click()
