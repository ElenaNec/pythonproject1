# Написать тест с использованием pytest и requests, в котором:
#
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
#
# conftest.py содержит фикстуру авторизации по адресу
# https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password" и возвращающей токен авторизации
#
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя, для этого выполняется get запрос по адресу
# https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации в параметре "X-Auth-Token".
# Для отображения постов другого пользователя передается "owner": "notMe".
#
# http://restapi.adequateshop.com/api/authaccount/registration
#
# http://restapi.adequateshop.com/api/authaccount/login

import requests
import yaml

with open(r'C:\Users\user\Desktop\pythonproject\Auto_test_python\Task2\config.yaml') as f:
    data = yaml.safe_load(f)


def get_list_id(token):
    url2 = data["url2"]
    list_id = []
    d = []
    res_get = requests.get(url=url2, headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    dict_get = res_get.json()
    d = dict_get.get('data')
    for elem in d:
        list_id.append(elem.get('id'))
    return list_id

