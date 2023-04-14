from utils.config.config import JSONReader


def test_get_valid_credentials():
    # We create an instance of the JSONReader class
    json_reader = JSONReader()

    # We obtain valid credentials from the config_user.json file
    valid_credentials = json_reader.get_value("user_valid_credentials")

    # We verify that the obtained credentials are the expected ones
    assert valid_credentials["email"] == "evans@gmail.com"
    assert valid_credentials["password"] == "123456"


def test_get_invalid_credentials():
    # We create an instance of the JSONReader class
    json_reader = JSONReader()

    # We obtain valid credentials from the config_user.json file
    invalid_credentials = json_reader.get_value("user_invalid_credentials")

    # We verify that the obtained credentials are the expected ones
    assert invalid_credentials["email"] == "evanstest@gmail.com"
    assert invalid_credentials["password"] == "654321"

