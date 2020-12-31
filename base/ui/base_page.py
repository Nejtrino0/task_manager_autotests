from webium.base_page import BasePage


class TaskManagerPage(BasePage):
    def __init__(self, driver, url):
        super(TaskManagerPage, self).__init__(driver=driver, url=url)
        self.driver = driver
        self.url = url

    @property
    def get_title(self):
        return self.driver.title


