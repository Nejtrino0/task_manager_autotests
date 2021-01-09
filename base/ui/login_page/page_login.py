from utils.decorators import wrap_all, step
from base.ui.base_page import TaskManagerPage
from locators.ui.login_page.locators import LoginPageLocators


@wrap_all(step)
class LoginPage(TaskManagerPage, LoginPageLocators):
    def __init__(self, driver, url):
        """Открываем страницу {0}"""
        super(LoginPage, self).__init__(driver=driver, url=''.join([url, 'login/']))
        self.open()

    def fill_username(self, *args):
        """Заполняем имя пользователя {0}"""
        self.username.send_keys(*args)

    def fill_password(self, *args):
        """Заполняем пароль {0}"""
        self.password.send_keys(*args)

    def click_login_button(self):
        """Нажимаем кнопку логина"""
        self.login_button.click()

    def click_register(self):
        """Нажимаем кнопку регистрации"""
        self.register.click()

    def click_forgot_password(self):
        """Нажимаем кнопку забыли пароль"""
        self.forgot_password.click()
