from webium import Find, Finds
from selenium.webdriver.common.by import By


class MainPageLocators:
    task_titles = Finds(value='div.media.mt-1 > div> h6')
    delete_task_icon = Finds(value='div.media.mt-1 > div> i.fa-trash-alt')
