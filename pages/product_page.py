from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    #переход в корзину
    def click_add_to_basket_btn(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    #проверка на совпадение названия книги с назвнием из сообщения об успехе
    def should_be_message_book_in_basket(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_IN_BASKET)
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        assert name_book.text == message.text, "Название книги в сообщении не совпадает с выбранной книгой!"

    #Проверка на совпадение цены корзины с ценой книги
    def should_be_price_in_basket(self):
        price_message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BASKET)
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        assert price_book.text == price_message.text, "Цена в корзине не совпадает с ценой книги!"

    #проверка, что нет сообщения
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BOOK_IN_BASKET), \
            "Success message is presented, but should not be"

    #проверка, что пропало сообщение
    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_BOOK_IN_BASKET), \
            "Success message is presented, but should not be"
