from pages.signup_login import SignupLogin
from playwright.sync_api import expect


def test_invalid_login(page):
    login = SignupLogin(page)
    login.go_signup_login()
    login.do_login(email="invalid_login@test.com", password="invalid_password")
    expect(page.get_by_text("Your email or password is")).to_be_visible()

def test_login_validation(page):
    login = SignupLogin(page)
    login.go_signup_login()
    login.do_login(email="kkowalska@test.com", password="123456789")
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    expect(page.get_by_text("Logged in as Katarzyna")).to_be_visible()

def test_logout(page):
    login = SignupLogin(page)
    login.go_home()
    login.button_logout.click()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()

def test_user_not_logged_in(page):
    login = SignupLogin(page)
    login.go_home()
    expect(page.get_by_role("link", name="Logout")).not_to_be_visible()