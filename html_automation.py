#!/usr/bin/env python3

from datetime import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
from getpass import getpass

client_id = input("Please input a client ID ")
username = input("Please input your username ")
password = getpass("Please input your password ")


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://ruralaz.servicept.com/")

user_input = browser.find_element_by_id('formfield-login')

user_input.send_keys(username)

password_input = browser.find_element_by_id('formfield-password')

password_input.send_keys(password)

submit_button = browser.find_element_by_id("LoginView.fbtn_submit")
sleep(3)
submit_button.click()
sleep(5)

access_client_point = browser.find_element_by_xpath("//*[@id=\"navigation-link.clientpt\"]")
access_client_point.click()

access_client_id = browser.find_element_by_xpath("//*[@id=\"ClientSearchView.clientId-textbox\"]")
access_client_id.send_keys(client_id)

submit_id_query = browser.find_element_by_xpath("//*[@id=\"ClientSearchView.clientIdSubmitBtn\"]/div")
submit_id_query.click()
