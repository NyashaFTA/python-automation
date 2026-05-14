from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DownloadsPage(BasePage):
    
    URL = "https://trueconf.ru/downloads/windows.html"

    # Локаторы
    # Кнопки
    WINDOWS_TAB_BUTTON = (By.XPATH, "//a[@href='https://trueconf.ru/downloads/windows.html']")
    MAC_TAB_BUTTON = (By.XPATH, "//a[@href='https://trueconf.ru/downloads/mac.html']")
    LINUX_TAB_BUTTON = (By.XPATH, "//a[@href='https://trueconf.ru/downloads/linux.html']")
    IOS_TAB_BUTTON = (By.XPATH, "//a[@href='https://trueconf.ru/downloads/ios.html']")
    ANDROID_TAB_BUTTON = (By.XPATH, "//a[@href='https://trueconf.ru/downloads/android.html']")
    AVRORA_TAB_BUTTON = (By.XPATH, "//a[@href='https://trueconf.ru/downloads/avrora.html']")
    ANDROID_TV_TAB_BUTTON = (By.XPATH, "//a[@href='https://trueconf.ru/downloads/android-tv.html']")
    WINDOWS_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "[data-tcw-download-test-id='toggle-download-modal']")
    MAC_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "[data-ga-event='trueconf_osx']")
    LINUX_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "[data-ga-event='trueconf_linux']")
    IOS_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "[data-ga-event='trueconf_ios']")
    ANDROID_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "[data-ga-event='trueconf_android']")
    AVRORA_DOWNLOAD_BUTTON = (By.XPATH, "//span[text()='Запросить доступ']")
    ANDROID_TV_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "[data-ga-event='trueconf_android']")

    # Маркеры
    WINDOWS_TAB_HEADER = (By.XPATH, "//h1[contains(text(),'Windows')]")
    MAC_TAB_HEADER = (By.XPATH, "//h1[contains(text(),'macOS')]")
    LINUX_TAB_HEADER = (By.XPATH, "//h1[contains(text(),'Linux')]")
    IOS_TAB_HEADER = (By.XPATH, "//h1[contains(text(),'Видеозвонки и конференции')]")
    ANDROID_TAB_HEADER = (By.XPATH, "//h1[contains(text(),'Android')]")
    AVRORA_TAB_HEADER = (By.XPATH, "//h1[contains(text(),'Аврора')]")
    ANDROID_TV_TAB_HEADER = (By.XPATH, "//h1[contains(text(),'Android TV')]")

    #Клиенты
    CLIENTS = {
        "mac": {
            "tab": MAC_TAB_BUTTON,
            "url": "https://trueconf.ru/downloads/mac.html",
            "header": MAC_TAB_HEADER,
            "download": MAC_DOWNLOAD_BUTTON
        },

        "linux": {
            "tab": LINUX_TAB_BUTTON,
            "url": "https://trueconf.ru/downloads/linux.html",
            "header": LINUX_TAB_HEADER,
            "download": LINUX_DOWNLOAD_BUTTON
        },

        "ios": {
            "tab": IOS_TAB_BUTTON,
            "url": "https://trueconf.ru/downloads/ios.html",
            "header": IOS_TAB_HEADER,
            "download": IOS_DOWNLOAD_BUTTON
        },

        "android": {
            "tab": ANDROID_TAB_BUTTON,
            "url": "https://trueconf.ru/downloads/android.html",
            "header": ANDROID_TAB_HEADER,
            "download": ANDROID_DOWNLOAD_BUTTON
        },

        "avrora": {
            "tab": AVRORA_TAB_BUTTON,
            "url": "https://trueconf.ru/downloads/avrora.html",
            "header": AVRORA_TAB_HEADER,
            "download": AVRORA_DOWNLOAD_BUTTON
        },

        "android_tv": {
            "tab": ANDROID_TV_TAB_BUTTON,
            "url": "https://trueconf.ru/downloads/android-tv.html",
            "header": ANDROID_TV_TAB_HEADER,
            "download": ANDROID_TV_DOWNLOAD_BUTTON
        },

        "windows": {
            "tab": WINDOWS_TAB_BUTTON,
            "url": "https://trueconf.ru/downloads/windows.html",
            "header": WINDOWS_TAB_HEADER,
            "download": WINDOWS_DOWNLOAD_BUTTON
        },
    }

    # Действия
    
    # Проверки
    def is_loaded(self):
        return self.wait_visible(self.WINDOWS_TAB_BUTTON)