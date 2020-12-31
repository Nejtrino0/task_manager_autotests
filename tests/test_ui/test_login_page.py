import pytest
from base.ui.login_page.page_login import LoginPage
from utils.api.utils import email


@pytest.mark.login_page
@pytest.mark.parametrize('driver', [LoginPage], indirect=['driver', ])
class TestLoginPage:
    def test_invalid_credentials(self, driver):
        driver.fill_username(email())
        driver.fill_password(email())
        driver.click_login_button()
        assert driver.is_element_present('login_button', timeout=20), \
            'Ошибка. Получилось залогиниться с невалидными кредами'

    def test_valid_credentials(self, driver):
        driver.fill_username('test_login')
        driver.fill_password('приветкакдела')
        if driver.is_element_present('login_button', timeout=20):
            driver.click_login_button()
        else:
            raise Exception('Кнопки Войти не была обнаружена')

        assert driver.get_title == 'Task Manager', 'Ошибка. Не получилось залогиниться с невалидными кредами'

    def test_empty_username_and_password(self, driver):
        driver.click_login_button()
        assert driver.get_title == 'Task Manager | Авторизация', \
            'Ошибка. Получилось залогиниться с пустыми полями имя пользователя и пароль'
