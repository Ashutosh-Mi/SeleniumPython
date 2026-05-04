from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.read_config import read_config


def get_driver():
    config = read_config()
    browser = config["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    else:
        raise Exception(f"Browser '{browser}' not supported")

    driver.maximize_window()
    driver.implicitly_wait(config["implicit_wait"])

    return driver