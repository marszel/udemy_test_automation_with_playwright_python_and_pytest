import pytest
from pages.base_page import BasePage
import pytest_html
from slugify import slugify
import os

STORAGE_FILE = "playwright/auth/state.json"

@pytest.fixture(scope='session')
def context(browser):
    if os.path.isfile(STORAGE_FILE):
        context = browser.new_context(
            base_url='https://automationexercise.com/',
            record_video_dir='videos',
            storage_state=STORAGE_FILE
        )
    else:
        context = browser.new_context(
            base_url='https://automationexercise.com/',
            record_video_dir='videos'
        )
    yield context
    os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)
    if not os.path.isfile(STORAGE_FILE):
        context.storage_state(path=STORAGE_FILE)
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

@pytest.fixture()
def accept_cookies(page):
    page.goto("")
    consent = BasePage(page)
    consent.click_consent()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook runs after each test phase.
    It checks for failures and attaches screenshots to the HTML report.
    """
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        try:
            if (report.skipped and xfail) or (report.failed and not xfail):
                screen_file = f"images/{slugify(item.nodeid)}.png"
                page = item.funcargs.get("page")
                if page:
                    page.screenshot(path=screen_file, full_page=True)
                    extras.append(pytest_html.extras.png(screen_file))
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
    report.extra = extras