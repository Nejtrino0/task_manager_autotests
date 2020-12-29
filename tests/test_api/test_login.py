import allure
import pytest
import requests
from utils.api.utils import email


@pytest.mark.api
@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestApiAuth:
    @pytest.mark.parametrize('data', [{"username": "test_auth", "password": "ghbdtn12345"}])
    def test_valid_auth(self, data, domain):
        with allure.step('Выполняем проверку авторизации с валидными данными'):
            assert requests.post(f'https://{domain}.herokuapp.com/api-token-auth/', data=data).json().get(
                'token', False), 'Не получилось авторизоваться с валидными кредами'

    @pytest.mark.parametrize('data', [{"username": email(), "password": email()}])
    def test_invalid_auth(self, data, domain):
        with allure.step('Выполняем проверку авторизации с не валидными данными'):
            assert not requests.post(f'https://{domain}.herokuapp.com/api-token-auth/', data=data).json().get(
                'token'), 'Получилось авторизоваться с не валидными кредами'

    @pytest.mark.parametrize('data', [{"username": "test_auth", "password": "ghbdtn12345"}])
    def test_response_is_ok(self, data, domain):
        with allure.step('Проверка на 200-й код'):
            assert requests.post(f'https://{domain}.herokuapp.com/api-token-auth/',
                                 data=data).ok, 'Сервер должен был вернуть 200-й статус код'

    def test_session_valid_auth(self, domain):
        session = requests.Session()
        headers = session.get(f'https://{domain}.herokuapp.com/login/').cookies.__dict__['_cookies'][
            'task-manager-3031.herokuapp.com']['/']['csrftoken'].__dict__['value']

        data = {"username": "test_auth", "password": "ghbdtn12345", "login": "Войти", "csrfmiddlewaretoken": headers}
        assert session.post('https://task-manager-3031.herokuapp.com/login/',
                            data=data).status_code == 200, 'Авторизация с валидными значениями не удалась'
