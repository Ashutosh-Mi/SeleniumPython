from selenium.webdriver.common.by import By

# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         # Locators
#         self.heading = (By.TAG_NAME, "h2")
#         self.username_input = (By.ID, "username")
#         self.password_input = (By.ID, "password")
#         self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
#         self.flash_message = (By.ID, "flash")

#     # Actions
#     def get_heading_text(self):
#         return self.driver.find_element(*self.heading).text

#     def enter_username(self, username):
#         self.driver.find_element(*self.username_input).send_keys(username)

#     def enter_password(self, password):
#         self.driver.find_element(*self.password_input).send_keys(password)

#     def click_login(self):
#         self.driver.find_element(*self.login_button).click()

#     def get_flash_message(self):
#         return self.driver.find_element(*self.flash_message).text
    
#################################################################################

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.heading = (By.TAG_NAME, "h2")
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.ID, "flash")

    def get_heading_text(self):
        return self.get_text(self.heading)

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

    def get_flash_message(self):
        return self.get_text(self.flash_message)