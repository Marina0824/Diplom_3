from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED = By.XPATH, "//h1[text()='Лента заказов']"
    ANY_ORDER = By.XPATH, "//a[contains(@class, 'OrderHistory_link')][1]"
    COMPOSITION = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"
    NUMBER_IN_FEED_ORDER = By.XPATH, "//p[@class='text text_type_digits-default'][1]"
    COUNT_ALL_TIME = By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p"
    COUNT_TODAY = By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p"
    ORDER_NUMBER_FROM_IN_PROGRESS = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text text_type_digits-default')]"
