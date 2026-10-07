from calendar import month
from pages.signup_login import SignupLogin


class Signup(SignupLogin):
    def __init__(self, page):
        super().__init__(page)
        self.checkbox_mr = page.get_by_role("radio", name="Mr.")
        self.checkbox_mrs = page.get_by_role("radio", name="Mrs.")
        self.input_name = page.get_by_role("textbox", name="Name *", exact=True)
        self.input_password = page.get_by_role("textbox", name="Password *")
        self.checkbox_page_sign_up_for_our_newsletter = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.checkbox_receive_special_offers_from = page.get_by_role("checkbox", name="Receive special offers from")
        self.select_day = page.locator("#days")
        self.select_month = page.locator("#months")
        self.select_year = page.locator("#years")
        self.input_first_name = page.get_by_role("textbox", name="First name *")
        self.input_last_name = page.get_by_role("textbox", name="Last name *")
        self.input_company = page.get_by_role("textbox", name="Company", exact=True)
        self.input_street_address = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.input_address_2 = page.get_by_role("textbox", name="Address 2")
        self.input_state = page.get_by_role("textbox", name="State *")
        self.input_state = page.get_by_role("textbox", name="City * Zipcode *")
        self.input_zipcode = page.locator("#zipcode")
        self_input_mobile_number = page.get_by_role("textbox", name="Mobile Number *")

    def fill_account_information(self, title="", name="", password="", date_of_birth="",
                                 sign_up_for_our_newsletter=True, receive_special_offers_from=True):
        if title == "Mr":
            self.checkbox_mr.check()
        elif title == "Mrs":
            self.checkbox_mrs.check()
        if name:
            self.input_name.fill(name)
        if password:
            self.input_password.fill(password)
        if date_of_birth:
            day, mo, year = date_of_birth.split("/")
            if day.startswith("0"):
                day = day[1:]
            if mo.startswith("0"):
                mo = mo[1:]
            self.select_day.select_option(day)
            self.select_month.select_option(mo)
            self.select_year.select_option(year)
        if sign_up_for_our_newsletter:
            self.checkbox_page_sign_up_for_our_newsletter.check()
        else:
            self.checkbox_page_sign_up_for_our_newsletter.uncheck()
        if receive_special_offers_from:
            self.checkbox_receive_special_offers_from.check()
        else:
            self.checkbox_receive_special_offers_from.uncheck()

    def fill_address_information(self, first_name, last_name, company, address, address_2, country, state, city,
                                 zipcode, mobile_number):
