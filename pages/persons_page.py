from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class PersonsPage(BasePage):

    URL = "https://trueconf.ru/persons"

    # Локаторы
    
    HEADER = (By.XPATH, "//h1[contains(text(),'Мой профиль')]")
    TORSO_BUTTON = (By.CSS_SELECTOR, ".header-menu__btn--user-login")
    ACCOUNT_DROPDOWN_LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href$='/logout/']")
    DOWNLOAD_IN_HEADER_BUTTON = (By.ID, 'hm-sbtn-1')
    DOWNLOAD_IN_DROPDOWN_BUTTON = (By.CLASS_NAME, 'header-menu__card-main')

    # Действия
    def click_torso_button(self):
        self.click(self.TORSO_BUTTON)
    
    def click_dropdown_logout_button(self):
        self.click(self.ACCOUNT_DROPDOWN_LOGOUT_BUTTON)

    def click_download_in_header_button(self):
        self.click(self.DOWNLOAD_IN_HEADER_BUTTON)
    
    def click_download_in_dropdown_button(self):
        self.click(self.DOWNLOAD_IN_DROPDOWN_BUTTON)

    def logout(self):

        self.is_loaded()

        self.click_torso_button()
        self.click_dropdown_logout_button()

    def go_to_downloads(self):

        self.click_download_in_header_button
        self.click_download_in_dropdown_button

    # Проверки

    def is_loaded(self):
        self.wait_visible(self.HEADER)