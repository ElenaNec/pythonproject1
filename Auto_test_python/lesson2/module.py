# модуль для инициализации Selenium webdriver
import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

with open(r"C:\Users\user\Desktop\pythonproject\Auto_test_python\lesson2\config.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


# Создадим класс, который будет управлять сайтом
class Site:
    # Инициализация сайта
    def __init__(self, address):
        # инициализация драйвера
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        # добавим ожидание
        self.driver.implicitly_wait(3)
        # откроем браузер развернутым на весь экран
        self.driver.maximize_window()
        # откроем адрес сайта
        self.driver.get(address)
        # подождем некоторое время, кот указано в config
        time.sleep(testdata['sleep_time'])

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "XPATH":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()