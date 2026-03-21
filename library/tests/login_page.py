from selenium.webdriver.common.by import By
from tests.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[text()='Login']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "button.nav-logout-btn")
    USERNAME_FIELD = (By.ID, "id_username")
    PASSWORD_FIELD = (By.ID, "id_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "li.error")

    def login(self, username, password):
        if not self.is_visible(self.USERNAME_FIELD, timeout=5):
            self.click(self.LOGIN_LINK)

        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)

    def logout(self):
        self.click(self.LOGOUT_LINK)

    def get_error_text(self):
        try:
            return self.find(self.ERROR_MESSAGE).text
        except TimeoutException:
            return ""

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False