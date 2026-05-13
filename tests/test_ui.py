from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.downloads_page import DownloadsPage
import requests
from pages.persons_page import PersonsPage
from pages.registration_page import RegistrationPage
import time

def test_login(driver, test_user):

    main_page = MainPage(driver)

    login_page = LoginPage(driver)

    persons_page = PersonsPage(driver)

    registration_page = RegistrationPage(driver)

    downloads_page = DownloadsPage(driver)

    main_page.open()

    assert main_page.is_download_button_in_header_visible()

    time.sleep(3) # а иначе в меня плюнет 503

    response = requests.get("https://trueconf.ru")
    assert response.status_code == 200

    main_page.click_torso_button()

    login_page.click_to_registration_button()

    registration_page.enter_username(test_user.login)
    registration_page.enter_password(test_user.password)
    registration_page.enter_email(test_user.email)
    registration_page.enter_full_name(test_user.full_name)

    registration_page.click_privacy_checkbox()
    
    registration_page.click_agreement_checkbox()

    registration_page.click_register_user_button()

    persons_page.logout()

    main_page.click_torso_button()

    login_page.wait_until_loaded()

    login_page.enter_login(test_user.login)
    login_page.enter_password(test_user.password)

    login_page.click_login_button()
    
    persons_page.wait_for_login()

    persons_page.click_download_in_header_button
    persons_page.click_download_in_dropdown_button

    for client_name, client_data in downloads_page.CLIENTS.items():

        downloads_page.safe_click(client_data["tab"])

        assert client_data["url"] in driver.current_url

        assert downloads_page.is_visible(client_data["header"])

        assert downloads_page.is_visible(client_data["download"])

    assert driver.current_url == "https://trueconf.ru/downloads/windows.html"

