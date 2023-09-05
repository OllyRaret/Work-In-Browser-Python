from .base_page import BasePage
from elements.main_page_elements import MainPageElements


class MainPage(BasePage):
    '''Главная страница'''
    def __init__(self, driver):
        self.driver = driver
        self.URL = 'https://eu.account.battle.net/login/ru/' # Передаем ей URL из задания
        self.elements = MainPageElements # Получаем нужные элементы страницы

    def load(self):
        self.driver.get(self.URL)

    def click_google(self):
        self.driver.find_element(*self.elements.GOOGLE_BUTTON).click()

    def set_email(self, email):
        pass

    def set_password(self, password):
        pass

    def confirm(self):
        pass
