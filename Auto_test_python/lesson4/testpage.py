import requests

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

# класс поиска локаторов
class TestSearchLocators:
    # нам надо из файла yaml получить пары тип локатора: локатор
    # заведем словарь
    ids = dict()
    with open(r"C:\Users\user\Desktop\pythonproject\Auto_test_python\lesson4\locators.yaml") as f:
        locators = yaml.safe_load(f)
    # нам нужно переделать разделы yaml так, что бы получились элементы пары
    # заполним локаторы, которые относятся к xpath
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    # вспомогательная функция для ввода текста
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self. find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    # вспомогательная функция получения текста
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # вспомогательная функция для клика
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_list_id(token):
        with open(r"C:\Users\user\Desktop\pythonproject\Auto_test_python\lesson4\config.yaml") as f:
            testdata = yaml.safe_load(f)
        list_id = []
        d = []
        try:
            res_get = requests.get(url=testdata["url2"], headers={"X-Auth-Token": token}, params={"owner": "notMe"})
        except:
            logging.exception(f"Exception get data")
            return False
        dict_get = res_get.json()
        d = dict_get.get('data')
        for elem in d:
            list_id.append(elem.get('id'))
        return list_id



    # методы ввода текска
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description="logging form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def enter_title_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_INPUT_TITLE"], word, description="input title form")

    def enter_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_INPUT_CONTENT"], word, description="input content form")


    # меотды получения текста
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])

    def get_text_blog(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RESULT_LOGIN"])

    def result_new_post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_RESULT_NEW_POST"])

    def get_alert_text(self):
        logging.info("Switch to alert")
        alert_text = self.switch_to_alert().text
        logging.info("Switch to alert is OK")
        return alert_text


    # методы клика
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST"], description="new post")

    def click_save_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_NEW_POST"], description="save")

    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT"], description="contact")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="contact us")







