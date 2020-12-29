import pytest
import requests
'api-token-auth/'

@pytest.mark.parametrize('login_params', [(number, 'hello') for number in range(1, 10)], scope="class",
                         indirect=['login_params'])
class TestNext:
    def test_1(self, login_params):
        print(login_params.login())

    def test_2(self, login_params):
        print()

    def test_3(self, login_params):
        print()

