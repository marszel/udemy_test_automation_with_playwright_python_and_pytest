from pages.products import Products
from pages.cart import Cart


def test_add_products_to_cart(page):
    products = Products(page)
    cart = Cart(page)
    products.go_product()
    products.add_product_to_cart(product_index="0")
    products.button_continue_shopping.click()
    products.add_product_to_cart(product_index="1")
    products.button_continue_shopping.click()
    products.button_cart.click()
    page.pause()
    cart.cart_validation(product_index=0, header="Blue Top", product_description="Women > Tops",
                         product_price="Rs. 500", product_total_price="Rs. 500")
    cart.cart_validation(product_index=1, header="Men Tshirt", product_description="Men > Tshirts",
                         product_price="Rs. 400", product_total_price="Rs. 400")

