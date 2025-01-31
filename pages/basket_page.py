from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    #тест на пустоту корзины
    def should_not_be_products_in_basket(self):
        assert self.summary_empty(*BasePageLocators.BASKET_PRODUCTS), \
            "Корзина не пуста"

    #тест на текст о пустоте корзины
    def should_is_basket_empty_message(self):
        assert self.basket_empty_message(), "Текст о пустоте корзины отсутствует"