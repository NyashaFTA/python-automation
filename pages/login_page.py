from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    URL = "https://trueconf.ru/login.html"

    # Локаторы
    HEADER = (By.XPATH, "//h1[contains(text(),'Для продолжения требуется авторизация')]")
    LOGIN_FIELD = (By.ID, "form-login")
    PASSWORD_FIELD = (By.ID, "form-password")
    LOGIN_BUTTON = (By.XPATH,"//button[text()='Войти']")
    TO_REGISTRATION_BUTTON = (By.CSS_SELECTOR,"a[href*='registration-standard']")

    # Действия
    def enter_login(self, login):

        field = self.wait_visible(self.LOGIN_FIELD)
        
        field.click()
        field.clear()
        field.type(login)
    
    def enter_password(self, password):
        self.wait_visible(
            self.PASSWORD_FIELD
        ).type(password)

    def click_login_button(self):
        self.wait_visible(
            self.LOGIN_BUTTON
        ).click()

    def click_to_registration_button(self):
        self.driver.find_element(
            *self.TO_REGISTRATION_BUTTON
        ).click()

    def wait_until_loaded(self):
        self.wait_visible(self.HEADER)

    # Проверки