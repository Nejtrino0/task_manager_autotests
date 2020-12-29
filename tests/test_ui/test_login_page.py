import pytest
from base.ui.login_page.page_login import LoginPage


@pytest.mark.login_page
@pytest.mark.parametrize('driver', [LoginPage], indirect=['driver', ])
class TestLoginPage:
    def test_invalid_credentials(self, driver):
        driver.click_login_button()



