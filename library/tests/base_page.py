from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.slow_mode = True

    def _slowdown(self):
        if self.slow_mode:
            time.sleep(3)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self._slowdown()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        element = self.find(locator)
        self._slowdown()
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

