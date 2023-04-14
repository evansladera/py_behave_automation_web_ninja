from utils.config.config import JSONReader


def test_get_value():
    json_reader = JSONReader()
    assert json_reader.get_value('user_valid_credentials')['email'] == 'evans@gmail.com'
    assert json_reader.get_value('user_valid_credentials')['password'] == '123456'
    assert json_reader.get_value('user_invalid_credentials')['email'] == 'evanstest@gmail.com'
    assert json_reader.get_value('user_invalid_credentials')['password'] == '654321'


def test_login_user_valid():
    json_reader = JSONReader()
    username, password = json_reader.login_user_valid()
    assert username == 'evans@gmail.com'
    assert password == '123456'


def test_login_user_invalid():
    json_reader = JSONReader()
    username, password = json_reader.login_user_invalid()
    assert username == 'evanstest@gmail.com'
    assert password == '654321'


