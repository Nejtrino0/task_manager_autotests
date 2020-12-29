from webium.base_page import BasePage
from locators.ui.login_page.locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):
    def __init__(self, driver, url):
        super(LoginPage, self).__init__(driver=driver, url=''.join([url, 'login/']))
        self.open()

    def fill_username(self, *args):
        self.username.send_keys(*args)

    def fill_password(self, *args):
        self.password.send_keys(*args)

    def click_login_button(self):
        self.login_button.click()
