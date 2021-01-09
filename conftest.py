import os
import pytest
from selenium.webdriver import DesiredCapabilities

import settings as sets
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webium import settings
from utils.utils import parse

allure_dir = parse(arg='--alluredir', default='./reports/ui/results/test_2')

settings.implicit_timeout = 30
settings.wait_timeout = 30

settings.default_search_type = By.CSS_SELECTOR


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()

    if not sets.DEBUG:
        options.add_argument('ignore-certificate-errors')
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--headless")
        options.add_argument("--disable-extensions")  # disabling extensions
        options.add_argument("--disable-gpu")  # applicable to windows os only
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.add_argument("disable-infobars")  # disabling infobars

    capabilities = DesiredCapabilities.CHROME
    capabilities["acceptInsecureCerts"] = True

    _driver = webdriver.Chrome(
        options=options,
        desired_capabilities=capabilities
    )
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


def pytest_sessionstart(session):
    pass


def pytest_sessionfinish(session, exitstatus):
    os.system('allure generate -c {0} -o ./reports/{2}/reports/{1}'.format(
        allure_dir,
        datetime.now().strftime('%d-%m-%Y_%H.%M.%S'),
        'ui' if 'ui' in allure_dir else 'api'
    ))
