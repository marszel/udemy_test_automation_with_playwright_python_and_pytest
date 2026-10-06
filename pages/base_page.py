class BasePage:
    def __init__(self, page):
        self.page = page
        self.button_home = page.get_by_role("link", name="Home")
        self.button_products = page.get_by_role("link", name="Products")
        self.button_cart = page.get_by_role("link", name="Cart")
        self.button_register_login = page.get_by_role("link", name="Signup / Login")

    def go_home(self):
        self.page.goto("https://www.automationexercise.com/")

    def go_cart(self):
        self.button_cart.click()

