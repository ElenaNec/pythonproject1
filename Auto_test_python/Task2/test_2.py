# проверка наличия поста
import yaml

with open(r'C:\Users\user\Desktop\pythonproject\Auto_test_python\Task2\config.yaml') as f:
    data = yaml.safe_load(f)


def test_id(return_token):
    find_id = data["id"]
    assert find_id and return_token


def test_description(return_token):
    find_id = data["id"]
    assert find_id and return_token