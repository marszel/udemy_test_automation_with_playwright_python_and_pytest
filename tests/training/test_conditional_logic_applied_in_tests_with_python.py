from pages.products import Products
from pages.cart import Cart


def test_add_product_to_cart_case_less_than_500(page):
    products = Products(page)
    products.go_product()
    product_price = int(products.product_card.nth(2).locator(".productinfo h2").inner_text().replace("Rs. ", ""))
    if product_price <= 500:
        products.add_product_to_cart(product_index=1)
        print("Product with value less than 500, added to the cart.")
    else:
        print("Product with value more than 500, not added to the cart.")

def test_delete_all_products_in_cart(page):
    cart = Cart(page)
    cart.go_cart()
    page.pause()
    while cart.button_delete_product.first.is_visible():
        cart.button_delete_product.first.click()
        page.wait_for_timeout(1000)

