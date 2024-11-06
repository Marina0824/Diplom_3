import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_move_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_account_in_header()
        personal_page = PersonalAccountPage(driver)
        personal_page.click_recovery_password()
        password_page = PasswordRecoveryPage(driver)
        assert password_page.check_presence_of_button_recover()

    @allure.title("Ввод почты и клик по кнопке Восстановить")
    def test_enter_email_click_recover(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_account_in_header()
        personal_page = PersonalAccountPage(driver)
        personal_page.click_recovery_password()
        password_page = PasswordRecoveryPage(driver)
        password_page.enter_email()
        password_page.click_button_recover()
        assert password_page.check_field_password()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_eye_button_makes_field_activ(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_account_in_header()
        personal_page = PersonalAccountPage(driver)
        personal_page.click_recovery_password()
        password_page = PasswordRecoveryPage(driver)
        password_page.enter_email()
        password_page.click_button_recover()
        password_page.enter_password()
        password_page.click_eye_button()
        assert password_page.check_field_password_active
