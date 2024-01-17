from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_item = page.locator('.cart_item')
