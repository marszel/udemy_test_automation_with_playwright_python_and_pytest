from pages.signup import Signup
from playwright.sync_api import expect

def test_register_new_user(page):
    signup = Signup(page)
    signup.go_home()
    page.pause()
    signup.button_register_login.click()
    expect(page.get_by_text("New User Signup!", exact=True)).to_be_visible()
    signup.do_signup(name="Jakub", email="jakub@test.com")
    expect(page.get_by_text("Enter Account Information", exact=True)).to_be_visible()
    signup.fill_account_information(title="Mr", password="123456", date_of_birth="08/08/2001",
                                    receive_special_offers_from=True, sign_up_for_our_newsletter=True)
    page.pause()