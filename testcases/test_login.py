import pytest
from pages.homepage import Homepage

class Test_Login:
    def test_successful_login(self, driver):
        username = "John Doe"
        password = "ThisIsNotAPassword"

        hp = Homepage(driver)
        hp.login(username, password)
        is_logged_in = hp.check_if_successfully_logged_in()
        hp.logout()
        assert is_logged_in

    def test_invalid_credentials(self, driver):
        username = "asbcs"
        password = "asdsad"

        hp = Homepage(driver)
        hp.login(username, password)
        hp.check_if_login_error_msg_displayed()