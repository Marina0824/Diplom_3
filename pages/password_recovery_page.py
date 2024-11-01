import allure
from pages.base_page import BasePage
from locators.passw_recovery_locators import PasswRecoveryLocators
from helper import create_email, create_password


class PasswordRecoveryPage(BasePage):
    @allure.step("Проверить наличие кнопки Восстановить")
    def check_presence_of_button_recover(self):
        return self.find_element(PasswRecoveryLocators.BUTTON_RECOVER)

    @allure.step("Ввести почту в поле Email")
    def enter_email(self):
        email = create_email()
        self.enter_text(PasswRecoveryLocators.FIELD_EMAIL, email)

    @allure.step("Нажать кнопку Восстановить")
    def click_button_recover(self):
        self.click_element(PasswRecoveryLocators.BUTTON_RECOVER)

    @allure.step("Проверить наличие поля Пароль")
    def check_field_password(self):
        return self.find_element(PasswRecoveryLocators.FIELD_PASSWORD)

    @allure.step("Ввести пароль в поле Пароль")
    def enter_password(self):
        password = create_password()
        self.enter_text(PasswRecoveryLocators.FIELD_PASSWORD, password)

    @allure.step("Нажать на иконку глаза")
    def click_eye_button(self):
        self.click_element(PasswRecoveryLocators.EYE_BUTTON)

    @allure.step("Проверить, что поле Пароль подсвечено")
    def check_field_password_active(self):
        return self.find_element(PasswRecoveryLocators.ACTIVE_FIELD_PASSWORD)
