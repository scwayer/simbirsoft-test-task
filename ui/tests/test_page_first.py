import os

from dotenv import load_dotenv
from ui.yandex_pages import YandexDisc

load_dotenv()

URL = os.environ.get("URL")
LOGIN = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")
FOLDER_NAME = os.environ.get("FOLDER_NAME")
FILE_TO_COPY = os.environ.get("FILE_TO_COPY")


def test_yandex_disc_first(browser):
    yandex_page = YandexDisc(browser)

    # Открыть страницу https://ya.ru
    yandex_page.got_to_site(URL)
    yandex_page.open_enter_page()

    # Авторизоваться
    yandex_page.enter_login(LOGIN)
    yandex_page.click_sign_button()
    yandex_page.enter_password(PASSWORD)
    yandex_page.click_sign_button()

    # Открыть Яндекс Диск
    yandex_page.open_disc()
    yandex_page.change_window(-1)

    # Создать новую папку и назвать ее
    yandex_page.create_new_folder(FOLDER_NAME)

    # Скопировать файл "Файл для копирования" в новую папку
    yandex_page.copy_file(FILE_TO_COPY, FOLDER_NAME)

    # Открыть папку
    yandex_page.open_folder(FOLDER_NAME)

    # Проверить наличие скопированного файла и его название
    files_list = yandex_page.get_files_list()
    assert len(files_list) > 0 and FILE_TO_COPY in files_list

    # Разлогиниться
    yandex_page.logout()
