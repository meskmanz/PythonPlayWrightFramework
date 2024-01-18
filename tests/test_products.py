import pytest
from playwright.sync_api import expect

from data.strings import ProductsStrings
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.ProductsPage import ProductsPage


@pytest.mark.usefixtures('login')
class TestProductsPage:

    def test_num_product_on_page(self, page):
        product_items_num = 6
        products_page = ProductsPage(page)
        expect(products_page.product_item).to_have_count(product_items_num)
        pass

    def test_add_products_to_cart(self, page):
        products_page = ProductsPage(page)
        products_page.add_products_to_card(3)
        expect(products_page.shopping_cart_badge).to_have_text(str(3))
        products_page.shopping_cart_link.click()
        cart_page = CartPage(page)
        expect(cart_page.cart_item).to_have_count(3)
        cart_page.checkout_btn.click()
        checkout_page = CheckoutPage(page)
        checkout_page.fill('Joe', 'Doe', 12345)
        checkout_page.finish_btn.click()
        expect(checkout_page.order_dispatched_msg).to_have_text(ProductsStrings().order_dispatched_msg)
