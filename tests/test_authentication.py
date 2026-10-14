from playwright.sync_api import expect
from pages.signup_login import SignupLogin
from pages.products import Products
from pages.cart import Cart


def teste_login(page):
    login = SignupLogin(page)
    login.go_signup_login()
    login.do_login(email='kkowalska@test.com', password='123456789')
    expect(page.get_by_role("link", name="Logout")).to_be_visible()

def test_add_products_to_cart(page):
    products = Products(page)
    products.go_product()
    products.add_product_to_cart(product_index='0')
    products.button_continue_shopping.click()
    products.add_product_to_cart(product_index='1')
    products.button_continue_shopping.click()
    page.pause()

def test_validate_cart(page):
    cart = Cart(page)
    cart.go_cart()
    cart.cart_validation(product_index='0', header='Blue Top', product_description='Women > Tops', product_price='Rs. 500', product_total_price='Rs. 500')
    cart.cart_validation(product_index='1', header='Men Tshirt', product_description='Men > Tshirts', product_price='Rs. 400', product_total_price='Rs. 400')
    page.pause()