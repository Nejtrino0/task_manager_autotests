import pytest
import settings as sets
from selenium import webdriver
from selenium.webdriver.common.by import By
from webium import settings

settings.implicit_timeout = 30
settings.wait_timeout = 30

settings.default_search_type = By.CSS_SELECTOR


@pytest.fixture
def driver(request):
    _driver = webdriver.Chrome()
    _driver.maximize_window()

    yield request.param(
        driver=_driver,
        url=sets.URLS['BASE_URL'].format(request.config.getoption("domain"))
    )

    _driver.quit()


def pytest_addoption(parser):
    parser.addoption('--domain', action='store', default='task-manager-3031',
                     help="Укажите домен")


@pytest.fixture(scope='class')
def domain(request):
    return request.config.getoption("domain")
