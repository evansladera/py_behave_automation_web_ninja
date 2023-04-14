# ---FILE: features/config/config_users.py---
import json
from utils.helpers import UserFilesPath


# class Users:
#     def __init__(self, config_file_users):
#         config_file_users = UserFilesPath.file_user_config
#         with open(config_file_users) as f:
#             user_data = json.load(f)
#         self.users_valid_email = user_data['user_valid_credentials']['email']
#         self.users_valid_password = user_data['user_valid_credentials']['password']
#         self.users_invalid_email = user_data['user_invalid_credentials']['email']
#         self.users_invalid_password = user_data['user_invalid_credentials']['password']
#
#     def login_user_valid(self):
#         username = self.users_valid_email
#         password = self.users_valid_password
#
#         return username, password
#
#     def login_user_invalid(self):
#         username = self.users_invalid_email
#         password = self.users_invalid_password
#
#         return username, password


class JSONReader:
    def __init__(self):
        self.filepath = UserFilesPath().file_user_config
        with open(self.filepath, 'r') as file:
            self.data = json.load(file)

        self.users_valid_email = self.data['user_valid_credentials']['email']
        self.users_valid_password = self.data['user_valid_credentials']['password']
        self.users_invalid_email = self.data['user_invalid_credentials']['email']
        self.users_invalid_password = self.data['user_invalid_credentials']['password']

    def get_value(self, key):
        return self.data[key]

    def login_user_valid(self):
        username = self.users_valid_email
        password = self.users_valid_password

        return username, password

    def login_user_invalid(self):
        username = self.users_invalid_email
        password = self.users_invalid_password

        return username, password
