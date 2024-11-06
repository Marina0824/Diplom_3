import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    @allure.step("Проверить наличие заголовка Лента Заказов")
    def check_header_order_feed(self):
        return self.find_element(OrderFeedLocators.ORDER_FEED)

    @allure.step("Нажать на любой заказ")
    def click_any_order(self):
        self.click_element(OrderFeedLocators.ANY_ORDER)

    @allure.step("Проверить наличие всплывающего окна с деталями заказа")
    def check_details_window(self):
        return self.find_element(OrderFeedLocators.COMPOSITION)

    @allure.step("Получить id верхнего заказа")
    def get_number_top_order(self):
        number_in_order_feed = self.get_text_of_element(OrderFeedLocators.NUMBER_IN_FEED_ORDER)
        return number_in_order_feed

    @allure.step("Подождать появления номера заказа в Ленте заказов")
    def wait_number_in_order_feed(self):
        return self.wait_element(OrderFeedLocators.NUMBER_IN_FEED_ORDER)

    @allure.step("Получить количество заказов, выполненное за все время")
    def get_count_all_time(self):
        return self.get_text_of_element(OrderFeedLocators.COUNT_ALL_TIME)

    @allure.step("Подождать появления количества заказов за все время")
    def wait_count_all_time(self):
        return self.wait_element(OrderFeedLocators.COUNT_ALL_TIME)

    @allure.step("Получить количество заказов, выполненное за сегодня")
    def get_count_today(self):
        return self.get_text_of_element(OrderFeedLocators.COUNT_TODAY)

    @allure.step("Подождать появления количества заказов за сегодня")
    def wait_count_today(self):
        return self.wait_element(OrderFeedLocators.COUNT_TODAY)

    @allure.step("Получить номер заказа из раздела В работе")
    def get_order_number_from_in_progress(self):
        return self.get_text_of_element(OrderFeedLocators.ORDER_NUMBER_FROM_IN_PROGRESS)

    @allure.step("Подождать появления номера заказа из раздела В работе")
    def wait_order_number_from_in_progress(self):
        return self.wait_element(OrderFeedLocators.ORDER_NUMBER_FROM_IN_PROGRESS)

    @allure.step("Проскроллить страницу да видимости количества заказов за сегодня")
    def scroll_to_count_today(self):
        self.scroll_to_element(OrderFeedLocators.COUNT_TODAY)
