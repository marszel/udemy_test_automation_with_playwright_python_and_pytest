from pages.signup_login import SignupLogin
from playwright.sync_api import expect

def test_login_validation(page):
    login = SignupLogin(page)
    login.go_signup_login()
    login.do_login(email="kkowalska@test.com", password="123456789")
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    page.pause()

def test_user_not_logged_in(page):
    login = SignupLogin(page)
    login.go_home()
    expect(page.get_by_role("link", name="Logout")).not_to_be_visible()
    page.pause()