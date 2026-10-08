import pytest
from pages.base_page import BasePage


@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(base_url="https://www.automationexercise.com/")
                                  #record_video_dir="videos")
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(30000)
    page.route("**/*googleads*/**", lambda route: route.abort())
    page.route("**/*doubleclick*/**", lambda route: route.abort())
    page.route("**/*adservice*/**", lambda route: route.abort())
    yield page
    page.close()

@pytest.fixture(autouse=True)
def accept_cookies(page):
    page.goto("")
    consent = BasePage(page)
    consent.click_consent()

