import time
import yaml
from testpage import OperationsHelper
import logging


with open(r"C:\Users\user\Desktop\pythonproject\Auto_test_python\lesson2\config.yaml") as f:
    testdata = yaml.safe_load(f)
    url = testdata['address']

def test_step1(browser):
    logging.info('Test_1 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info('Test_2 Starting')
    testpage = OperationsHelper(browser, url)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_text_blog() == "Blog"

def test_step3(browser):
    # залогиниться
    # logging.info('Test_3 Starting')
    testpage = OperationsHelper(browser, url)
    # testpage.go_to_site()
    # testpage.enter_login(testdata['login'])
    # testpage.enter_pass(testdata['password'])
    # testpage.click_login_button()
    # создание поста
    testpage.click_new_post_button()
    testpage.enter_title_post("СУПЕР НОВЫЙ ПОСТ")
    testpage.enter_content_post("test")
    testpage.click_save_new_post_button()
    time.sleep(2)
    assert testpage.result_new_post() == "СУПЕР НОВЫЙ ПОСТ"


def test_step4(browser):
    logging.info('Test_4 Starting')
    # залогиниться
    testpage = OperationsHelper(browser, url)
    # testpage.go_to_site()
    # testpage.enter_login(testdata['login'])
    # testpage.enter_pass(testdata['password'])
    # testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(1)
    testpage.click_contact_us_button()
    time.sleep(1)
    assert testpage.get_alert_text() == "Form successfully submitted"


