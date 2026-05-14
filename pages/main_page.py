from selenium.webdriver.common.by import By
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

    def is_download_in_header_button_visible(self):
        self.wait_visible(self.DOWNLOAD_IN_HEADER_BUTTON)
    
    def is_download_in_dropdown_button_visible(self):
        self.wait_visible(self.DOWNLOAD_IN_DROPDOWN_BUTTON)
    
    # Проверки
    def is_loaded(self):
        return self.wait_visible(self.DOWNLOAD_IN_HEADER_BUTTON)