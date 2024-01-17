from pages.BasePage import BasePage


class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_label = page.locator('xpath=//div[@class="header_secondary_container"]/span')
        self.product_item = page.locator('.inventory_item')
        self.add_to_cart_btn = page.locator('xpath=//div[@class="inventory_item"]//button')
        self.shopping_cart_badge = page.locator('.shopping_cart_badge')
        self.shopping_cart_link = page.locator('.shopping_cart_link')
