from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_BOOK_IN_BASKET = (By.CSS_SELECTOR, '#messages strong')
    MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, '#messages p strong')
    NAME_BOOK = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_BOOK = (By.CSS_SELECTOR, '.product_main .price_color')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p")
