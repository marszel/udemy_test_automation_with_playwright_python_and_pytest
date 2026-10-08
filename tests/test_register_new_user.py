from pages.signup import Signup
from playwright.sync_api import expect

def test_register_new_user(page):
    signup = Signup(page)
    signup.go_home()
    signup.button_register_login.click()
    expect(page.get_by_text("New User Signup!", exact=True)).to_be_visible()
    signup.do_signup(name="Jakub", email="jakub@test.com")
    expect(page.get_by_text("Enter Account Information", exact=True)).to_be_visible()
    signup.fill_account_information(title="Mr", password="123456", date_of_birth="08/08/2001",
                                    receive_special_offers_from=True, sign_up_for_our_newsletter=True)
    signup.fill_address_information(first_name="Jakub", last_name="Nowak", company="Test Company", address="Test Street", country="United States", state="New York",city="New York",zipcode="10001", mobile_number="234234234")
    signup.button_create_account.click()
    expect(page.get_by_text("Account Created!")).to_be_visible()
    signup.button_continue.click()
    expect(page.get_by_text("Logged in as Jakub")).to_be_visible()

def test_delete_user(page):
    signup = Signup(page)
    signup.go_home()
    signup.button_delete_account.click()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()


