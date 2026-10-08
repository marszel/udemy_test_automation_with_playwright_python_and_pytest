from pages.base_page import BasePage


class Products(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_card = page.locator(".single-products")
        self.button_add_to_cart = page.locator(".overlay-content:visible .btn")
        self.button_continue_shopping = page.get_by_role("button", name="Continue Shopping")

    def add_product_to_cart(self, product_index=0):
        self.product_card.nth(product_index).hover()
        self.button_add_to_cart.nth(product_index).click()
