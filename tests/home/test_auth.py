import pytest
from pages.home.login_page import LoginPage

@pytest.mark.usefixtures("one_time_set_up", "set_up")
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.driver = one_time_set_up
        self.login_page = LoginPage(self.driver) # не забываем self!

    def test_empty_email_field(self):
        self.login_page.click_login_screen_button()
        self.login_page.click_login_button()
        assert bool(self.login_page.error_blank()) == True

    def test_title(self):
        title = self.login_page.verify_title_name()
        assert title == True

    @pytest.mark.parametrize("test_data", ['TEST'])
    def test_name(self, test_data):
        name = 'TEST'
        assert name == test_data

    @pytest.mark.parametrize("email", [('rwur@erwre.22',)])
    def test_invalid_code(self, email):
        self.login_page.enter_email(email)
        self.login_page.click_login_button()
        self.login_page.verify_code()
        assert bool(self.login_page.invalid_code_error()) == True