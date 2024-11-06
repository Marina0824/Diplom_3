from selenium.webdriver.common.by import By


class PasswRecoveryLocators:
    BUTTON_RECOVER = By.XPATH, "//button[text()='Восстановить']"
    FIELD_EMAIL = By.XPATH, "//input[@class='text input__textfield text_type_main-default']"
    FIELD_PASSWORD = By.XPATH, "//input[@name='Введите новый пароль']"
    EYE_BUTTON = By.XPATH, "//div[@class='input__icon input__icon-action']"
    ACTIVE_FIELD_PASSWORD = By.XPATH, "//div[contains(@class, 'input_status_active')]"
