import requests


class YandexDisc:

    def __init__(self, oauth_token, headers):
        self.oauth_token = oauth_token
        self.headers = headers
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"

    def create_new_folder(self, folder_name):
        params = {
            "path": folder_name
        }
        response = requests.put(url=self.base_url, headers=self.headers, params=params)
        return response.status_code, response.json()

    def copy_file_to_folder(self, file_name_to_copy, file_name_of_copy):
        url = self.base_url + "/copy"
        params = {
            "from": file_name_to_copy,
            "path": file_name_of_copy
        }
        response = requests.post(url=url, headers=self.headers, params=params)
        return response.status_code, response.json()

    def rename_file(self, old_file_name, new_file_name):
        url = self.base_url + "/move"
        params = {
            "from": old_file_name,
            "path": new_file_name
        }
        response = requests.post(url=url, headers=self.headers, params=params)
        return response.status_code, response.json()

    def check_file(self, file_name):
        params = {
            "path": file_name
        }
        response = requests.get(url=self.base_url, headers=self.headers, params=params)
        return response.status_code
