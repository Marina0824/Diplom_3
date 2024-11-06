import allure
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.order_feed_page import OrderFeedPage


class TestMainPage:
    @allure.title("Проверить переход по клику на Конструктор")
    def test_click_on_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_account_in_header()
        personal_page = PersonalAccountPage(driver)
        personal_page.click_constructor()
        assert main_page.check_header_construct_burger()

    @allure.title("Проверить переход по клику на Лента заказов")
    def test_click_on_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_page = OrderFeedPage(driver)
        assert order_page.check_header_order_feed()

    @allure.title("Проверить всплывающее окно с деталями по клику на ингредиент")
    def test_open_window_order_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        assert main_page.check_order_details()

    @allure.title("Проверить закрытие всплывающего окна с ингредиентом нажатием на крестик")
    def test_close_window_by_click_x(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        main_page.click_x_in_order_details()
        assert main_page.check_close_order_details

    @allure.title("Проверить увеличение каунтера ингредиента при его добавлении в заказ")
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_to_constructor()
        assert main_page.get_count_of_ingredient() == '2'

    @allure.title("Проверить, что залогиненный пользователь может оформить заказ")
    def test_login_user_can_order(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_to_constructor()
        main_page.click_button_place_order()
        assert main_page.check_window_id_order()
