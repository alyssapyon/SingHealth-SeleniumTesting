import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import json

from CONSTANTS import *

# set wait time between testcases
waitTime = 1

# file to store registered accounts
# filename = "registeredAccounts.json"
filename = registeredAccounts_filepath


# NEED TO EDIT THIS BASED ON WHERE YOUR CHROMEDRIVER IS
PATH = chromeDriver_filepath

driver = webdriver.Chrome(PATH)


def test_login(keys_username, keys_password):
    driver.get("http://127.0.0.1:8000/logout/")

    try:
        # username
        input_username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        input_username.clear()
        input_username.send_keys(keys_username)

        # password
        input_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        input_password.clear()
        input_password.send_keys(keys_password)

        # press enter
        input_password.send_keys(Keys.RETURN)

        # print statements
        print("keys_username: " + keys_username)
        print("keys_password: " + keys_password)

        if (driver.title == "SingHealth WebApp"):
            isValid = True
            print("TESTCASE: VALID! LOGGED IN	✓")
        else:
            isValid = False
            print("TESTCASE: FAILED, CANNOT LOG IN")
        print()

        time.sleep(waitTime)
    except:
        print("TEST FAILED TO RUN")
        time.sleep(5)
        driver.quit()


def run_test_valid_login(times):
    with open(filename, "r+") as file:
        data = json.load(file)

    for i in range(times):
        temp = data['accounts']
        if len(temp) < 1:
            test_login(admin_username,  admin_password)
        else:
            account = random.choice(temp)
            test_login(account['username'], account['password'])

    file.close()


# run_test_valid_login(10)


# # Opening JSON file
# f = open(filename)

# # returns JSON object as
# # a dictionary
# data = json.load(f)

# # Iterating through the json
# # list
# for i in data['accounts']:
#     username = i['username']
#     password = i['password']
#     test_login(username, password)


# # Closing file
# # f.close()
# username = "AY@ZrgQ_jaSQUGLf9UFaYkLur1rjZh6V9KqvzYHFbvVevH25@BEpjTTWb1zaHSmFM6Scq3swFI4J97RG+buRZGdq.r-QQDnh.1FE_XWiwXlFSo1HR@.zarK6eiU1k3dDYXdO-vxV15Cl4ORu_8yq1ZUZasi.Bj@oHVeuzmOXFMAOORTxg5RvH-QFgcVoQjaQDocBJlbBcxZXlNe297RbgSe9VXyIkj1nVFdanUwgp@LAp3P.8BTvpxtSaddYrVKa"
# password = "P5P;p;JDT>-D0\DYG0'p" + '"'+"`cV~nEv=z*f)*8wt"
# test_login(username, password)
