from lib2to3.pgen2 import driver
from math import prod
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)
browser.get('https://saucedemo.com')


user_name_input = WebDriverWait(browser,timeout = 10).until(lambda d: d.find_element(By.ID,"user-name"))
user_name_input.send_keys("standard_user")
password_input = WebDriverWait(browser,timeout = 10).until(lambda d: d.find_element(By.ID,"password"))
password_input.send_keys("secret_sauce")
login_button = WebDriverWait(browser,timeout = 10).until(lambda d: d.find_element(By.CSS_SELECTOR,"#login-button"))
login_button.click()
#time.sleep(3)

product_title = browser.find_element(By.CLASS_NAME,"title")
assert product_title.is_displayed()
assert product_title.text == "PRODUCTS"

menu_button = browser.find_element(By.CSS_SELECTOR,"#react-burger-menu-btn")
menu_button.click()
logout_button = WebDriverWait(browser,timeout = 10).until(lambda d: d.find_element(By.CSS_SELECTOR,"#logout_sidebar_link"))
logout_button.click()


login_button_logout = WebDriverWait(browser,timeout = 10).until(lambda d: d.find_element(By.CSS_SELECTOR,"#login-button"))
assert login_button_logout.is_displayed()

browser.close()