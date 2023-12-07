from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

# класс поиска локаторов
class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")

    LOCATOR_RESULT_LOGIN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    LOCATOR_CREATE_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_INPUT_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_INPUT_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_NEW_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_RESULT_NEW_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")



class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click loging button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_text_blog(self):
        blog = self.find_element(TestSearchLocators.LOCATOR_RESULT_LOGIN, time=3)
        text_blog = blog.text
        logging.info(f"We find text {text_blog} in error field {TestSearchLocators.LOCATOR_RESULT_LOGIN[1]}")
        return text_blog

    def click_new_post_button(self):
        logging.info("Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST).click()

    def enter_title_post(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_INPUT_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content_post(self, word):
        logging.info(f"send {word} to element {TestSearchLocators.LOCATOR_INPUT_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_save_new_post_button(self):
        logging.info("Click save button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_NEW_POST).click()

    def result_new_post(self):
        post = self.find_element(TestSearchLocators.LOCATOR_RESULT_NEW_POST, time=3)
        text_post = post.text
        logging.info(f"We find text {text_post} in error field {TestSearchLocators.LOCATOR_RESULT_NEW_POST[1]}")
        return text_post


#######

    def click_contact_button(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

    def click_contact_us_button(self):
        logging.info("Click contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert_text(self):
        logging.info("Switch to alert")
        alert_text = self.switch_to_alert().text
        logging.info("Switch to alert is OK")
        return alert_text
