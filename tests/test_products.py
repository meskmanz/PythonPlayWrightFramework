import pytest
from playwright.sync_api import expect

from pages.CartPage import CartPage
from pages.ProductsPage import ProductsPage


@pytest.mark.usefixtures('login')
class TestProductsPage:

    def test_num_product_on_page(self, setup):
        product_items_num = 6
        products_page = ProductsPage(setup)
        expect(products_page.product_item).to_have_count(product_items_num)
        pass

    def test_add_products_to_cart(self, setup):
        products_page = ProductsPage(setup)
        products = products_page.add_to_cart_btn.all()[:3]
        for item in products:
            item.click()
        expect(products_page.shopping_cart_badge).to_have_text(str(3))
        products_page.shopping_cart_link.click()
        cart_page = CartPage(setup)
        expect(cart_page.cart_item).to_have_count(len(products))
        pass
