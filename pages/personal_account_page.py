import allure
from pages.base_page import BasePage
from locators.personal_acc_locators import PersonalAccLocators
from urls import URL, ORDER_HISTORY, LOGIN


class PersonalAccountPage(BasePage):
    @allure.step("Внизу страницы нажать Восстановить пароль")
    def click_recovery_password(self):
        self.click_element(PersonalAccLocators.LINK_RECOVERY_PASSWORD)

    @allure.step("Ввести почту в поле Email")
    def enter_email(self, email):
        self.enter_text(PersonalAccLocators.EMAIL_FIELD, email)

    @allure.step("Ввести пароль в поле Пароль")
    def enter_password(self,password):
        self.enter_text(PersonalAccLocators.PASSWORD_FIELD, password)

    @allure.step("Нажать кнопку Войти")
    def click_button_enter(self):
        self.click_element(PersonalAccLocators.BUTTON_ENTER)

    @allure.step("Проверить наличие кнопки Выход")
    def check_button_logout(self):
        return self.find_element(PersonalAccLocators.BUTTON_LOGOUT)

    @allure.step("Нажать на Историю заказов")
    def click_order_history(self):
        self.click_element(PersonalAccLocators.ORDER_HISTORY)

    @allure.step("Сравнить текущий url и url Истории заказов")
    def check_order_history_url(self):
        expected_url = URL+ORDER_HISTORY
        return self.check_current_url(expected_url)

    @allure.step("Нажать кнопку Выход")
    def click_button_logout(self):
        self.click_element(PersonalAccLocators.BUTTON_LOGOUT)

    @allure.step("Сравнить текущий url и url страницы авторизации")
    def check_login_page_url(self):
        expected_url = URL+LOGIN
        return self.check_current_url(expected_url)

    @allure.step("Нажать Конструктор")
    def click_constructor(self):
        self.click_element(PersonalAccLocators.CONSTRUCTOR)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        number_in_history = self.get_text_of_element(PersonalAccLocators.NUMBER_IN_HISTORY)
        return number_in_history

    @allure.step("Нажать на Историю заказов")
    def click_java_order_history(self):
        self.click_java(PersonalAccLocators.ORDER_HISTORY)

    @allure.step("Подождать появления Истории заказов")
    def wait_order_history(self):
        return self.wait_element(PersonalAccLocators.ORDER_HISTORY)

    @allure.step("Подождать появления номера заказа в Истории заказов")
    def wait_number_in_history(self):
        return self.wait_element(PersonalAccLocators.NUMBER_IN_HISTORY)
