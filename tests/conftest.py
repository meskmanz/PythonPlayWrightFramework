from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright, expect

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption('--bn', action='store', default="chromium", help="Choose browser: chromium or firefox")
    parser.addoption('--h', action='store', default=False, help='Choose headless: True or False')
    parser.addoption('--s', action='store', default={'width': 1920, 'height': 1080}, help='Size window: width,height')
    parser.addoption('--slow', action='store', default=200, help='Choose slow_mo for robot action')


@fixture()
def setup(request):
    url = 'https://www.saucedemo.com'
    headless = eval(request.config.getoption("h"))
    slow_mo = request.config.getoption("slow")
    with sync_playwright() as playwright:
        if request.config.getoption("bn") == 'chromium':
            browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
        elif request.config.getoption("bn") == 'firefox':
            browser = playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
        else:
            browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        yield page
        context.close()
        browser.close()


@fixture(autouse=False)
def login(setup):
    login_page = LoginPage(setup)
    login_page.login('standard_user', 'secret_sauce')
    products_page = ProductsPage(setup)
    expect(products_page.product_label).to_be_visible()
