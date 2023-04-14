import os


class UserFilesPath:
    def __init__(self):
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.file_user_config = os.path.join(self.root_dir, 'utils', 'config', 'config_user.json')

