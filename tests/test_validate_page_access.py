from pages.base_page import BasePage
from playwright.sync_api import expect


def test_validate_home(page, accept_cookies):
    """
    -Access the homepage
    -Validate the header "AutomationExercise" to be visible
    """
    print(test_validate_home.__doc__)
    view = BasePage(page)
    view.go_home()
    expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

def test_validate_products(page, accept_cookies):
    """
    -Access the product page
    -Validate the image "Website for practice" to be visible
    """
    print(test_validate_products.__doc__)
    view = BasePage(page)
    view.go_product()
    expect(page.get_by_role("img", name="Website for practice")).to_be_visible()

def test_validate_cart(page, accept_cookies):
    """
    -Access the cart page
    -Validate the text "Home Shopping Cart" to be visible
    """
    print(test_validate_cart.__doc__)
    view = BasePage(page)
    view.go_cart()
    expect(page.get_by_text("Home Shopping Cart")).to_be_visible()

def test_validate_login(page, accept_cookies):
    """
    -Access the login page
    -Validate a header "Login to your account" to be visible
    """
    print(test_validate_login.__doc__)
    view = BasePage(page)
    view.go_signup_login()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()