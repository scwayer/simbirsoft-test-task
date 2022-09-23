import os

from dotenv import load_dotenv
from api.utils import YandexDisc

load_dotenv()

OAUTH_TOKEN = os.environ.get("OAUTH_TOKEN")
FOLDER_NAME = os.environ.get("FOLDER_NAME")
FILE_TO_COPY = os.environ.get("FILE_TO_COPY")

NEW_FILE_TO_COPY_NAME = f"{FOLDER_NAME}/Переименовал.docx"
PATH_TO_COPY = f"{FOLDER_NAME}/{FILE_TO_COPY}"

headers = {
    "Accept": "application/json",
    "Authorization": "OAuth " + OAUTH_TOKEN
}


def test_yandex_disc():
    yandex_disc = YandexDisc(OAUTH_TOKEN, headers)

    # Выполнить запрос на создание новой папки с названием
    yandex_disc.create_new_folder(FOLDER_NAME)

    # Скопировать файл "Файл для копирования" в созданную папку
    yandex_disc.copy_file_to_folder(FILE_TO_COPY, PATH_TO_COPY)

    # Переименовать файл
    status_code, body = yandex_disc.rename_file(PATH_TO_COPY, NEW_FILE_TO_COPY_NAME)

    # Файл успешно переименован
    assert yandex_disc.check_file(NEW_FILE_TO_COPY_NAME) == 200

    # Код ответа
    expected_body = {
        "href": "https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2Fnew+folder%2F%D0%9F%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB.docx",
        "method": "GET",
        "templated": False
    }
    assert status_code == 201

    # Тело ответа
    assert body == expected_body
