from selenium.webdriver.common.by import By


class MainPageLocators:
    LINK_PERSONAL_ACCOUNT = By.XPATH, "//a[@href='/account']"
    CONSTRUCT_BURGER = By.XPATH, "//h1[text()='Соберите бургер']"
    ORDER_FEED = By.XPATH, "//a[@href='/feed']"
    FIRST_INGREDIENT = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')][1]"
    ORDER_DETAILS = By.XPATH, "//h2[text()='Детали ингредиента']"
    BUTTON_X = By.XPATH, "//button[@type='button']"
    BURGER_BASKET = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]"
    COUNTER = By.XPATH, "//p[contains(@class, 'counter_counter__num')]"
    BUTTON_PLACE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"
    ID_ORDER = By.XPATH, "//p[text()='идентификатор заказа']"
    BUTTON_X_ID_ORDER_WINDOW = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]"
