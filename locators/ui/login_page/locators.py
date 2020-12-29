from webium import Find
from selenium.webdriver.common.by import By


class LoginPageLocators:
    username = Find(by=By.ID, value='email_address')
    password = Find(by=By.ID, value='password')
    login_button = Find(value='input[name=login]')
