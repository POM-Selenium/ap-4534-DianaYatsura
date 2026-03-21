from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.login_page import LoginPage
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTest(StaticLiveServerTestCase):
    def setUp(self):
        User.objects.create_user(
            email="test@test.com",
            password="0207",
            first_name="Test",
            last_name="User"
        )

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))

        self.driver.implicitly_wait(0)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_full_auth_flow(self):
        self.driver.get(self.live_server_url)

        self.login_page.login("test@test.com", "0207")

        self.assertTrue(self.login_page.is_visible(self.login_page.LOGOUT_LINK))

        self.login_page.logout()

        self.login_page.login("test@test.com", "0208")
        self.assertFalse(self.login_page.is_visible(self.login_page.LOGOUT_LINK, timeout=2))

