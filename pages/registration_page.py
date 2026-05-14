from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):

    URL = "https://trueconf.ru/products/online/registration-standard.html"

    # Локаторы

    USERNAME_FIELD = (By.ID, "person-reg-login")
    PASSWORD_FIELD = (By.ID, "person-reg-password")
    EMAIL_FIELD = (By.ID, "person-reg-email")
    FULL_NAME_FIELD = (By.ID, "person-reg-full_name")
    PRIVACY_CHECKBOX = (By.ID, "person-reg-privacy_policy")
    AGREEMENT_CHECKBOX = (By.ID, "person-reg-personal_data_processing_consent_checkbox")
    REGISTER_USER_BUTTON = (By.ID, "html")


    # Действия
    def enter_username(self, login):
        self.driver.find_element(
            *self.USERNAME_FIELD
        ).type(login)
    
    def enter_password(self, password):
        self.driver.find_element(
            *self.PASSWORD_FIELD
        ).type(password)

    def enter_email(self, email):
        self.driver.find_element(
            *self.EMAIL_FIELD
        ).type(email)

    def enter_full_name(self, full_name):
        self.driver.find_element(
            *self.FULL_NAME_FIELD
        ).type(full_name)

    def click_privacy_checkbox(self):
        self.click(self.PRIVACY_CHECKBOX)

    def click_agreement_checkbox(self):
        self.click(self.AGREEMENT_CHECKBOX)

    def click_register_user_button(self):
        self.click(self.REGISTER_USER_BUTTON)

    # Проверки