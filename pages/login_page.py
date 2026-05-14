from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://trueconf.ru/login.html"

    # Локаторы
    HEADER = (By.XPATH, "//h1[contains(text(),'Для продолжения требуется авторизация')]")
    LOGIN_FIELD = (By.ID, "form-login")
    PASSWORD_FIELD = (By.ID, "form-password")
    LOGIN_BUTTON = (By.XPATH,"//button[text()='Войти']")
    GO_TO_REGISTRATION_FORM_BUTTON = (By.CSS_SELECTOR,"a[href*='registration-standard']")

    # Действия
    def enter_login(self, login):
        self.type(self.LOGIN_FIELD, login)
    
    def enter_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def go_to_registration(self):
        self.click(self.GO_TO_REGISTRATION_FORM_BUTTON)

    def login(self, user):
        self.enter_login(user.login)
        self.enter_password(user.password)
        self.click_login_button()

    # Проверки
    def is_loaded(self):
        return self.wait_visible(self.LOGIN_FIELD)