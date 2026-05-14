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

    login_page.go_to_registration()

    registration_page.registration(test_user)

    persons_page.logout()

    main_page.click_torso_button()

    login_page.is_loaded()

    login_page.login(test_user)

    login_page.click_login_button()
    
    persons_page.is_loaded()

    persons_page.go_to_downloads()

    for client_name, client_data in downloads_page.CLIENTS.items():

        downloads_page.click(client_data["tab"])

        assert client_data["url"] in driver.current_url

        assert downloads_page.wait_visible(client_data["header"])

        assert downloads_page.wait_visible(client_data["download"])

    assert driver.current_url == "https://trueconf.ru/downloads/windows.html"

