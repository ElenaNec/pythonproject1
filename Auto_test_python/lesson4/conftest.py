import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from email_report import send_email
import requests
from testpage import OperationsHelper



with open(r"C:\Users\user\Desktop\pythonproject\Auto_test_python\lesson4\config.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


# Инициализация сайта
@pytest.fixture(scope='session')
def browser():
    # инициализация драйвера
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# отправка отчета на почту по завершению всех тестов
@pytest.fixture(autouse=True, scope='session')
def sendemail():
    yield
    send_email()


@pytest.fixture(autouse=True)
def return_token():
    result = requests.post(url=testdata["url"], data={"username": testdata["login"], "password": testdata["password"]})
    token = result.json()["token"]
    return OperationsHelper.get_list_id(token)

