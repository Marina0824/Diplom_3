import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title("Переход по клику на Личный кабинет")
    def test_click_to_personal_account(self, driver, login_user):
        main_page = MainPage(driver)
        personal_page = PersonalAccountPage(driver)
        main_page.click_personal_account_in_header()
        assert personal_page.check_button_logout()

    @allure.title("Переход в раздел История заказов")
    def test_move_to_order_history(self, driver, login_user):
        main_page = MainPage(driver)
        personal_page = PersonalAccountPage(driver)
        main_page.click_personal_account_in_header()
        personal_page.click_order_history()
        current_url = personal_page.check_order_history_url()
        assert current_url is True

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, login_user):
        main_page = MainPage(driver)
        personal_page = PersonalAccountPage(driver)
        main_page.click_personal_account_in_header()
        personal_page.click_button_logout()
        current_url = personal_page.check_login_page_url()
        assert current_url is True
