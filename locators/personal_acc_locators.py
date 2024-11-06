from selenium.webdriver.common.by import By


class PersonalAccLocators:
    LINK_RECOVERY_PASSWORD = By.XPATH, "//a[@href='/forgot-password']"
    EMAIL_FIELD = By.XPATH, "//input[@name='name']"
    PASSWORD_FIELD = By.XPATH, "//input[@name='Пароль']"
    BUTTON_ENTER = By.XPATH, "//button[text()='Войти']"
    BUTTON_LOGOUT = By.XPATH, "//button[text()='Выход']"
    ORDER_HISTORY = By.XPATH, "//a[@href='/account/order-history']"
    CONSTRUCTOR = By.XPATH, "//a[@href='/']"
    NUMBER_IN_HISTORY = By.XPATH, "//p[@class='text text_type_digits-default']"
