import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:
    @allure.title("Проверить открытие всплывающего окна с деталями, если нажать на заказ")
    def test_click_order_open_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_page = OrderFeedPage(driver)
        order_page.click_any_order()
        assert order_page.check_details_window

    @allure.title("Проверить отображение заказа из Истории заказов в Ленте заказов")
    def test_order_from_history_show_to_order_feed(self, driver, login_user_and_make_order):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        personal_page = PersonalAccountPage(driver)
        main_page.click_java_personal_account_in_header()
        personal_page.wait_order_history()
        personal_page.click_java_order_history()
        personal_page.wait_number_in_history()
        number_in_history = personal_page.get_order_number()
        main_page.click_order_feed()
        order_page.wait_number_in_order_feed()
        number_in_order_feed = order_page.get_number_top_order()
        assert number_in_history == number_in_order_feed

    @allure.title("Проверить при создании заказа увеличение счетчика Выполнено за все время")
    def test_counter_all_time_increased(self, driver, login_user):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        personal_page = PersonalAccountPage(driver)
        main_page.click_order_feed()
        order_page.wait_count_all_time()
        before = order_page.get_count_all_time()
        personal_page.click_constructor()
        main_page.drag_and_drop_ingredient_to_constructor()
        main_page.click_button_place_order()
        main_page.close_window_with_id_order()
        main_page.click_java_order_feed()
        order_page.wait_count_all_time()
        after = order_page.get_count_all_time()
        assert before < after

    @allure.title("Проверить при создании заказа уселичение счетчика Выполнено за сегодня")
    def test_counter_today_increased(self, driver, login_user):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        personal_page = PersonalAccountPage(driver)
        main_page.click_order_feed()
        order_page.wait_count_today()
        order_page.scroll_to_count_today()
        before = order_page.get_count_today()
        personal_page.click_constructor()
        main_page.drag_and_drop_ingredient_to_constructor()
        main_page.click_button_place_order()
        main_page.close_window_with_id_order()
        main_page.click_java_order_feed()
        order_page.wait_count_today()
        after = order_page.get_count_today()
        assert before < after

    @allure.title("Проверить после оформления заказа, что его номер появляется в разделе В работе")
    def test_order_number_in_list_in_progress(self, driver, login_user_and_make_order):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        personal_page = PersonalAccountPage(driver)
        main_page.click_java_personal_account_in_header()
        personal_page.wait_order_history()
        personal_page.click_java_order_history()
        personal_page.wait_number_in_history()
        order_number = personal_page.get_order_number()
        order_number = order_number.replace('#', '')
        main_page.click_order_feed()
        order_page.wait_order_number_from_in_progress()
        order_number_in_progress = order_page.get_order_number_from_in_progress()
        assert order_number == order_number_in_progress
