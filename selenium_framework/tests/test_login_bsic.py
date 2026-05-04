# from selenium import webdriver

# def test_open_login_page():
#     driver = webdriver.Chrome()

#     driver.get("https://the-internet.herokuapp.com/login")

#     assert "login" in driver.title.lower()

#     driver.quit()


# import time
# def test_open_login_page(driver):
#     driver.get("https://the-internet.herokuapp.com/login")
#     # time.sleep(30)
#     input("Press Enter to close the browser")
#     assert "login" in driver.title.lower()
##########################################################

# from selenium.webdriver.common.by import By
# from utils.read_config import read_config

# def test_open_login_page(driver):
#     config = read_config()

#     driver.get(config["base_url"])

#     # assert "login" in driver.title.lower()
#     heading = driver.find_element(By.TAG_NAME, "h2").text
#     assert heading == "Login Page"
#     #assert "Login Page" in driver.page_source
    
    ##################################################################

# from utils.read_config import read_config
# from pages.login_page import LoginPage

# def test_open_login_page(driver):
#     config = read_config()

#     driver.get(config["base_url"])

#     login_page = LoginPage(driver)

#     # Validate heading
#     heading = login_page.get_heading_text()
#     assert heading == "Login Page"

#     # Optional: Test login
#     login_page.enter_username("tomsmith")
#     login_page.enter_password("SuperSecretPassword!")
#     login_page.click_login()

#     flash_message = login_page.get_flash_message()
#     assert "You logged into a secure area!" in flash_message

    ##################################################################

# import pytest
# from utils.read_config import read_config
# from utils.read_testdata import get_login_data
# from pages.login_page import LoginPage


# @pytest.mark.parametrize("data", get_login_data())
# def test_login_data_driven(driver, data):
#     config = read_config()

#     driver.get(config["base_url"])

#     login_page = LoginPage(driver)

#     login_page.enter_username(data["username"])
#     login_page.enter_password(data["password"])
#     login_page.click_login()

#     message = login_page.get_flash_message()

#     assert data["expected"] in message
#####################################################################

import allure
import pytest
from utils.read_config import read_config
from utils.read_testdata import get_login_data
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("data", get_login_data())
def test_login_data_driven(driver, data):
    logger.info(f"Starting test with user: {data['username']}")

    config = read_config()
    driver.get(config["base_url"])

    login_page = LoginPage(driver)

    logger.info("Entering username and password")
    # login_page.enter_username(data["username"])
    # login_page.enter_password(data["password"])
    login_page.login(data["username"], data["password"])
    #login_page.click_login()

    message = login_page.get_flash_message()
    logger.info(f"Received message: {message}")

    assert data["expected"] in message



@allure.step("Opening login page")
def open_login(driver, url):
    driver.get(url)