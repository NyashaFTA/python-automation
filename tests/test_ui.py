import requests
import time
from pages.downloads_page import DownloadsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.persons_page import PersonsPage
from pages.registration_page import RegistrationPage

def test_login(driver, test_user):

    main_page = MainPage(driver)

    login_page = LoginPage(driver)

    persons_page = PersonsPage(driver)

    registration_page = RegistrationPage(driver)

    downloads_page = DownloadsPage(driver)

    main_page.open()

    assert main_page.is_loaded()

    time.sleep(3) # А иначе плюёт 503

    response = requests.get("https://trueconf.ru")
    assert response.status_code == 200

    main_page.click_torso_button()

    login_page.is_loaded()

    login_page.go_to_registration()

    registration_page.is_loaded()

    registration_page.registration(test_user)

    persons_page.is_loaded()

    persons_page.logout()

    main_page.is_loaded()

    main_page.click_torso_button()

    login_page.is_loaded()

    login_page.login(test_user)

    login_page.click_login_button()
    
    persons_page.is_loaded() 

    persons_page.go_to_downloads()

    for client_name in downloads_page.CLIENTS:

        assert downloads_page.is_client_available(client_name)

    assert driver.current_url == "https://trueconf.ru/downloads/windows.html"

