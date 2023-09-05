from .main_page import MainPage
from .email_page import EmailPage
from .password_page import PasswordPage
from .smart_page import SmartPage


class AuthPage(SmartPage):
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.main_page.load() # Загружаем начальную страницу

    def get_expected_title(self):
        return 'Авторизация в Battle.net'

    def get_expected_final_title(self):
        return 'Обзор учетной записи'

    def login_google(self, email, password):
        '''Аутентификация через Google по данным пользователя'''
        # Вход через Google
        assert self.is_loaded()
        self.main_page.click_google()

        # Ввод электронной почты
        login_page = EmailPage(self.driver)
        login_page.set_email(email)
        login_page.confirm()

        # Ввод пароля
        # password_page = PasswordPage(self.driver)
        # password_page.set_password(password)
        # password_page.confirm()
