import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_step_8 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

#может ли гость добавить товар в корзину
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.should_be_message_book_in_basket()
    page.should_be_price_in_basket()

#3 теста с ожиданием на отсутствие сообщения о добавлении товара в коризну
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.should_disappeared()

#проверка на присутсвие ссылки на страницу входа и регистрации
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_step_8)
    page.open()
    page.should_be_login_link()

#проверка на переход на страницу входа и регистрации
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = BasePage(browser, link_step_8)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

#тест, что корзина пуста
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link_step_8)
    page.open()
    page.go_to_basket()
    page.should_not_be_products_in_basket()
    page.should_is_basket_empty_message()

#тесты с участием регистрации пользователя
@pytest.mark.new
class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_be_message_book_in_basket()
        page.should_be_price_in_basket()
