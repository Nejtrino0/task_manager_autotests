import re

from webium.wait import wait

from base.ui.base_page import TaskManagerPage
from locators.ui.main_page.locators import MainPageLocators


class MainPage(TaskManagerPage, MainPageLocators):
    def __init__(self, driver, url):
        super(MainPage, self).__init__(driver=driver, url=url)
        self.open()

    def get_title_text(self, text):
        return list(filter(lambda title: re.findall(text, title), self.task_titles))

    def click_delete_icon(self, index):
        wait(
            lambda: self.delete_task_icon[index].click() is None,
            waiting_for='Ждем пока иконка удаления задачи станет кликабельной'
        )
