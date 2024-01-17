from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.firstname_field = page.locator('#first-name')
        self.lastname_field = page.locator('#last-name')
        self.postalcode_field = page.locator('#postal-code')
        self.continue_btn = page.locator('#continue')
        self.finish_btn = page.locator('#finish')
        self.order_dispatched_msg = page.locator('.complete-text')

    def fill(self, firstname, lastname, postalcode):
        self.firstname_field.type(firstname)
        self.lastname_field.type(lastname)
        self.postalcode_field.type(str(postalcode))
        self.continue_btn.click()
