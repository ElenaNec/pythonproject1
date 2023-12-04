import yaml
from selenium.webdriver.common.keys import Keys
import time

with open(r"C:\Users\user\Desktop\pythonproject\Auto_test_python\lesson2\config.yaml") as f:
    testdata = yaml.safe_load(f)

def test_step1(site, log_xpath, passw_xpath, btn_xpath, result_xpath):
    # найдем эл-т воода (верхнее поле) по XPATH
    input1 = site.find_element("XPATH", log_xpath)
    input1.send_keys("test")

    input2 = site.find_element("XPATH", passw_xpath)
    input2.send_keys("test")

    btn = site.find_element("XPATH", btn_xpath)
    btn.click()

    err_label = site.find_element("XPATH", result_xpath)
    assert err_label.text == "401"

def test_step2(site, log_xpath, passw_xpath, btn_xpath, result_login):
    input1 = site.find_element("XPATH", log_xpath)
    input1.send_keys(testdata["login"])

    input2 = site.find_element("XPATH", passw_xpath)
    input2.send_keys(testdata["password"])

    btn = site.find_element("XPATH", btn_xpath)
    btn.click()

    poz_label = site.find_element("XPATH", result_login)
    assert poz_label.text == "Blog"


def test_step3(site, log_xpath, passw_xpath, btn_xpath, create_post_xpath, input_title, result_new_post, save_new_post):
    input1 = site.find_element("XPATH", log_xpath)
    input1.send_keys(testdata["login"])

    input2 = site.find_element("XPATH", passw_xpath)
    input2.send_keys(testdata["password"])

    btn = site.find_element("XPATH", btn_xpath)
    btn.click()

    click_plus = site.find_element("XPATH", create_post_xpath)
    time.sleep(testdata['sleep_time'])
    click_plus.click()
    time.sleep(testdata['sleep_time'])

    enter_title = site.find_element("XPATH", input_title).send_keys("СУПЕР НОВЫЙ ПОСТ")
    time.sleep(testdata['sleep_time'])
    save_post = site.find_element("XPATH",save_new_post)
    save_post.click()
    time.sleep(testdata['sleep_time'])

    result_post = site.find_element("XPATH", result_new_post)
    assert result_post.text == "СУПЕР НОВЫЙ ПОСТ"




# def test_step1():
#     # найдем эл-т воода (верхнее поле) по XPATH
#     x_selector1 = """//*[@id="login"]/div[1]/label/input"""
#     input1 = site.find_element("XPATH", x_selector1)
#     # отправим неправильную информацию в верхнее поле ввода
#     input1.send_keys("test")
#
#     # найдем эл-т воода (нижнее поле) по XPATH
#     x_selector2 = """//*[@id="login"]/div[2]/label/input"""
#     input2 = site.find_element("XPATH", x_selector2)
#     # отправим неправильную информацию в нижнее поле ввода
#     input2.send_keys("test")
#
#     # найдем кнопку login по css
#     btn_selector = "button "
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#
#
#     # найдем элемент "вывод ошибки"
#     x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
#     err_label = site.find_element("XPATH", x_selector3)
#     assert err_label.text == "401"


