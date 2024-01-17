from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright, expect

from data.environment import Environment
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from utils.file import add_allure_env


def pytest_addoption(parser):
    parser.addoption('--bn', action='store', default="chromium", help="Choose browser: chromium or firefox")
    parser.addoption('--h', action='store', default=False, help='Choose headless: True or False')
    parser.addoption('--s', action='store', default={'width': 1920, 'height': 1080}, help='Size window: width,height')
    parser.addoption('--slow', action='store', default=200, help='Choose slow_mo for robot action')


@fixture()
def browser(request):
    headless = request.config.getoption("h")
    if not isinstance(headless, bool):
        headless = eval(headless)
    slow_mo = request.config.getoption("slow")
    with sync_playwright() as playwright:
        if request.config.getoption("bn") == 'chromium':
            browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
            add_allure_env('Browser', 'Chromium')
        elif request.config.getoption("bn") == 'firefox':
            browser = playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
            add_allure_env('Browser', 'Firefox')
        else:
            browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
            add_allure_env('Browser', 'Chromium')
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@fixture()
def page(browser):
    browser.goto(Environment().get_base_url())
    return browser


@fixture(autouse=False)
def login(page):
    login_page = LoginPage(page)
    login_page.login('standard_user', 'secret_sauce')
    products_page = ProductsPage(page)
    expect(products_page.product_label).to_be_visible()
