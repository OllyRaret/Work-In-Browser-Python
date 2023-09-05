from abc import ABC, abstractmethod


class BasePage(ABC):
    '''Базовый класс страницы'''
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def load(self):
        '''Загрузка страницы'''
        pass

    @abstractmethod
    def set_email(self, email):
        '''Ввод электронной почты в соответствующее поле'''
        pass

    @abstractmethod
    def set_password(self, password):
        '''Ввод пароля в соответствующее поле'''
        pass

    @abstractmethod
    def confirm(self):
        '''Нажатие кнопки "Далее"'''
        pass

    @abstractmethod
    def click_google(self):
        '''Нажатие на кнопку "Вход через Google"'''
        pass
