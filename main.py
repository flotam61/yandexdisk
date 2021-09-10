import requests
import os
import yadisk

class YaUploader:
    def __init__(self, token: str):
        self.token = "AQAAAAAUxqCcAADLWz8udiiRREVSkH-fQmYrqIA"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        directory = file_path
        file1 = os.listdir(directory)
        global file
        for file in file1:
            href = self.get_upload_link(disk_file_path=file_path).get("href", "")
            response = requests.put(href, data=open(file_path + "/" + file, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file, "overwrite": True}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()



if __name__ == '__main__':
    path_to_file = 'C:/Users/Максим/PycharmProjects/httpdz3/DZ2'
    token = "AQAAAAAUxqCcAADLWz8udiiRREVSkH-fQmYrqIA"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

