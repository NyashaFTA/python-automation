from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        element = self.wait_visible(locator, timeout)
        element.click()

    def type(self, locator, text, timeout=10, clear=True):
        element = self.wait_visible(locator, timeout)
        if clear:
            element.clear()
        element.type(text)

    def get_text(self, locator, timeout=10):
        element = self.wait_visible(locator, timeout)
        return element.text