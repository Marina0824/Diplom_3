import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("В шапке сайта нажать Личный кабинет")
    def click_personal_account_in_header(self):
        self.click_element(MainPageLocators.LINK_PERSONAL_ACCOUNT)

    @allure.step("Проверить наличие заголовка Соберите бургер")
    def check_header_construct_burger(self):
        return self.find_element(MainPageLocators.CONSTRUCT_BURGER)

    @allure.step("Нажать на Лента заказов")
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED)

    @allure.step("Нажать на первый ингредиент")
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Проверить наличие заголовка Детали ингредиента")
    def check_order_details(self):
        return self.find_element(MainPageLocators.ORDER_DETAILS)

    @allure.step("Нажать на Х во всплывающем окне")
    def click_x_in_order_details(self):
        self.click_element(MainPageLocators.BUTTON_X)

    @allure.step("Проверить закрытия окна с деталями ингредиента")
    def check_close_order_details(self):
        return self.is_element_invisible(MainPageLocators.ORDER_DETAILS)

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_and_drop_ingredient_to_constructor(self):
        source_element = self.find_element(MainPageLocators.FIRST_INGREDIENT)
        target_element = self.find_element(MainPageLocators.BURGER_BASKET)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step("Получить количество ингредиентов")
    def get_count_of_ingredient(self):
        return self.get_text_of_element(MainPageLocators.COUNTER)

    @allure.step("Нажать на кнопку Оформить заказ")
    def click_button_place_order(self):
        self.click_element(MainPageLocators.BUTTON_PLACE_ORDER)

    @allure.step("Проверить наличие всплывающего окна с идентификатором заказа")
    def check_window_id_order(self):
        return self.find_element(MainPageLocators.ID_ORDER)

    @allure.step("Закрыть всплывающее окно с id заказа")
    def close_window_with_id_order(self):
        self.click_java(MainPageLocators.BUTTON_X_ID_ORDER_WINDOW)

    @allure.step("В шапке сайта нажать Личный кабинет")
    def click_java_personal_account_in_header(self):
        self.click_java(MainPageLocators.LINK_PERSONAL_ACCOUNT)

    @allure.step("Нажать на Лента заказов")
    def click_java_order_feed(self):
        self.click_java(MainPageLocators.ORDER_FEED)
