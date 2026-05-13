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
        self.safe_click(self.TORSO_BUTTON)
    
    def click_dropdown_logout_button(self):
        self.safe_click(self.ACCOUNT_DROPDOWN_LOGOUT_BUTTON)

    def wait_for_login(self):

        WebDriverWait(self.driver, 10).until(
            lambda d: "persons" in d.current_url
        )
    
    def click_download_in_header_button(self):
        self.click(self.DOWNLOAD_IN_HEADER_BUTTON)
    
    def click_download_in_dropdown_button(self):
        self.click(self.DOWNLOAD_IN_DROPDOWN_BUTTON)

    def wait_until_loaded(self):
        self.find_visible(self.HEADER)
    
    def logout(self):

        self.wait_until_loaded()

        self.click_torso_button()
        self.click_dropdown_logout_button()
    # Проверки