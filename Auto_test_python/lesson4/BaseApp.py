import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver, url):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                                message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exeption")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f"property {property} not found in element with locator {locator}")
            return None


    def go_to_site(self):
        self.driver.maximize_window()
        try:
             start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exeception while open site")
            start_browsing = None
        return start_browsing


    def switch_to_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert
        except:
            logging.exception("Exeption with alert")
            return None

