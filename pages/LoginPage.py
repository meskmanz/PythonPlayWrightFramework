from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = page.locator('#user-name')
        self.password_field = page.locator('#password')
        self.login_btn = page.locator('#login-button')
        self.error_msg = page.locator('xpath=//h3[@data-test="error"]')

    def login(self, username, password):
        self.username_field.type(username)
        self.password_field.type(password)
        self.login_btn.click()
