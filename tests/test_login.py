from playwright.sync_api import expect

from data.strings import LoginStrings
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


class TestLoginPage:

    def test_invalid_crds(self, page):
        login_page = LoginPage(page)
        login_page.login('wrong_usrname', 'wrong_pswd')
        expect(login_page.error_msg).to_contain_text(LoginStrings().invalid_creds_msg)

    def test_valid_crds(self, page):
        login_page = LoginPage(page)
        login_page.login('standard_user', 'secret_sauce')
        products_page = ProductsPage(page)
        expect(products_page.product_label).to_be_visible()
