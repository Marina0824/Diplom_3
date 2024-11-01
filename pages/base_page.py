from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    def check_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    def is_element_invisible(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))
        return True

    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    def click_java(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
