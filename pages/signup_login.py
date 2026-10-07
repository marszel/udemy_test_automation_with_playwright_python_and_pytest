from pages.base_page import BasePage


class SignupLogin(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.input_email_login = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.input_password_login = page.get_by_role("textbox", name="Password")
        self.button_login = page.get_by_role("button", name="Login")
        self.input_name_signup = page.get_by_role("textbox", name="Name")
        self.input_email_signup = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.button_signup = page.get_by_role("button", name="Signup")

    def do_login(self, email="", password=""):
        self.input_email_login.fill(email)
        self.input_password_login.fill(password)
        self.button_login.click()

    def do_signup(self, name="", email=""):
        self.input_name_signup.fill(name)
        self.input_email_signup.fill(email)
        self.button_signup.click()
