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
        self.type(self.USERNAME_FIELD, login)
    
    def enter_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def enter_email(self, email):
        self.type(self.EMAIL_FIELD, email)

    def enter_full_name(self, full_name):
        self.type(self.FULL_NAME_FIELD, full_name)

    def click_privacy_checkbox(self):
        self.click(self.PRIVACY_CHECKBOX)

    def click_agreement_checkbox(self):
        self.click(self.AGREEMENT_CHECKBOX)

    def click_register_user_button(self):
        self.click(self.REGISTER_USER_BUTTON)
    
    def registration(self, user):
        self.enter_username(user.login)
        self.enter_password(user.password)
        self.enter_email(user.email)
        self.enter_full_name(user.full_name)
        self.click_privacy_checkbox()
        self.click_agreement_checkbox()
        self.click_register_user_button()

    # Проверки