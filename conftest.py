import pytest
import helper
from selenium import webdriver
from urls import URL
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        ValueError("Не удается создать экземпляр для этого браузера")
    browser.get(URL)
    browser.maximize_window()
    yield browser
    browser.quit()

#Создание и удаление пользователя по API
@pytest.fixture
def create_user_and_delete():
    email, password, token = helper.create_new_user()
    yield email, password, token
    helper.delete_user(token)

@pytest.fixture
def login_user(driver, create_user_and_delete):
    email, password, token = create_user_and_delete
    main_page = MainPage(driver)
    main_page.click_personal_account_in_header()
    personal_page = PersonalAccountPage(driver)
    personal_page.enter_email(email)
    personal_page.enter_password(password)
    personal_page.click_button_enter()

@pytest.fixture
def login_user_and_make_order(driver, create_user_and_delete):
    email, password, token = create_user_and_delete
    main_page = MainPage(driver)
    main_page.click_personal_account_in_header()
    personal_page = PersonalAccountPage(driver)
    personal_page.enter_email(email)
    personal_page.enter_password(password)
    personal_page.click_button_enter()
    main_page.drag_and_drop_ingredient_to_constructor()
    main_page.click_button_place_order()
    main_page.close_window_with_id_order()
