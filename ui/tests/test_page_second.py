import os

from dotenv import load_dotenv
from ui.yandex_pages import YandexDisc

load_dotenv()

URL = os.environ.get("URL")
LOGIN = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")
FOLDER_NAME = os.environ.get("FOLDER_NAME")
FILE_TO_COPY = os.environ.get("FILE_TO_COPY")
UPLOADED_FILE_PATH = os.environ.get("UPLOADED_FILE_PATH")
UPLOADED_FILE_NAME = os.environ.get("UPLOADED_FILE_NAME")


def test_yandex_disc_second(browser):
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

    # Открыть папку
    yandex_page.open_folder(FOLDER_NAME)

    # Загрузить файл расширения .txt с текстом
    yandex_page.upload_file(UPLOADED_FILE_PATH)

    # Открыть файл
    yandex_page.open_file(UPLOADED_FILE_NAME)
    yandex_page.change_window(-1)

    # Проверить текст в файле
    text = yandex_page.get_text_from_file()
    for index, line in enumerate(open(UPLOADED_FILE_PATH).readlines()):
        assert text[index] == line.strip()

    # Разлогиниться
    yandex_page.logout_from_file()
