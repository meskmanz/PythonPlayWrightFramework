from playwright.sync_api import expect

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


class TestLoginPage:

    def test_invalid_crds(self, page):
        text = 'Epic sadface: Username and password do not match any user in this service'
        login_page = LoginPage(page)
        login_page.login('wrong_usrname', 'wrong_pswd')
        expect(login_page.error_msg).to_contain_text(text)

    def test_valid_crds(self, page):
        login_page = LoginPage(page)
        login_page.login('standard_user', 'secret_sauce')
        products_page = ProductsPage(page)
        expect(products_page.product_label).to_be_visible()
