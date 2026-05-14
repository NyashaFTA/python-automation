from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class MainPage(BasePage):

    URL = "https://trueconf.ru/"

    # Локаторы
    DOWNLOAD_IN_HEADER_BUTTON = (By.ID, 'hm-sbtn-1')
    DOWNLOAD_IN_DROPDOWN_BUTTON = (By.CLASS_NAME, 'header-menu__card-main')
    TORSO_BUTTON = (By.CSS_SELECTOR, ".header-menu__btn--user-login")
    ACCOUNT_DROPDOWN_LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href$='/logout/']")

    # Действия
    def open(self):
        self.driver.get(self.URL)

    def click_download_in_header_button(self):
        self.click(self.DOWNLOAD_IN_HEADER_BUTTON)
    
    def click_download_in_dropdown_button(self):
        self.click(self.DOWNLOAD_IN_DROPDOWN_BUTTON)

    def click_torso_button(self):
        self.click(self.TORSO_BUTTON)
    
    def click_dropdown_logout_button(self):
        self.click(self.ACCOUNT_DROPDOWN_LOGOUT_BUTTON)

    # Проверки
    def is_download_button_in_header_visible(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
          EC.visibility_of_element_located(self.DOWNLOAD_IN_HEADER_BUTTON)
        )

        return element.is_displayed()
    
    def is_download_button_in_dropdown_visible(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
          EC.visibility_of_element_located(self.DOWNLOAD_IN_DROPDOWN_BUTTON)
        )

        return element.is_displayed()