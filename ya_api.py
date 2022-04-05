import requests


class YaApi:
    def __init__(self, token: str):
        self.token = token

    def __get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_directory(self, dir_name: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.__get_headers()
        params = {"path": dir_name, "overwrite": "true"}
        response = requests.put(url=url, params=params, headers=headers)
        response_json = response.json()
        return response.status_code, response_json

    def get_directory_info(self, dir_name: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.__get_headers()
        params = {"path": dir_name, "overwrite": "true"}
        response = requests.get(url=url, params=params, headers=headers)
        response_json = response.json()
        return response.status_code, response_json

    def delete_directory(self, dir_name: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.__get_headers()
        params = {"path": dir_name, "overwrite": "true"}
        response = requests.delete(url=url, params=params, headers=headers)
        return response.status_code
