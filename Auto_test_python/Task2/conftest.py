import pytest
import requests
import yaml
from task2 import get_list_id


with open(r'C:\Users\user\Desktop\pythonproject\Auto_test_python\Task2\config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture(autouse=True)
def return_token():
    url = data["url"]
    login = data["login"]
    password = data["password"]
    result = requests.post(url=url, data={"username": login, "password": password})
    token = result.json()["token"]
    return get_list_id(token)



