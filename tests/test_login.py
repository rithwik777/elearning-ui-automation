import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

        login = LoginPage(self.driver)
        login.login("student", "Password123")  # valid creds

        # Assert success
        assert "Logged In Successfully" in self.driver.page_source
        assert "Log out" in self.driver.page_source
