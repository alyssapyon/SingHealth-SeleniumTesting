import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import json

from gen_username_valid import generate_username_valid
from gen_email_valid import generate_email_valid
from gen_password_valid import generate_password_valid
from gen_username_INvalid import *

from CONSTANTS import *

# set wait time between testcases
waitTime = 2

# file to store registered accounts
filename = registeredAccounts_filepath

# NEED TO EDIT THIS BASED ON WHERE YOUR CHROMEDRIVER IS
PATH = chromeDriver_filepath
driver = webdriver.Chrome(PATH)


def test_register(keys_username, keys_email, keys_password1, same, group):
    dictionary = {}

    driver.get("http://127.0.0.1:8000/logout/")

    if group == "admin":
        driver.get("http://127.0.0.1:8000/register/admin")
    elif group == "tenant":
        driver.get("http://127.0.0.1:8000/register/tenant")
    else:
        print("ERROR! wrong group name")
        return 0

    try:
        # username
        input_username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        input_username.clear()
        input_username.send_keys(keys_username)

        # email
        input_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        input_email.clear()
        input_email.send_keys(keys_email)

        # password1
        input_password1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password1"))
        )
        input_password1.clear()
        input_password1.send_keys(keys_password1)

        # password2
        input_password2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password2"))
        )
        input_password2.clear()
        if same == True:
            input_password2.send_keys(keys_password1)
        else:
            input_password2.send_keys(generate_password_valid())

        # press enter
        input_password2.send_keys(Keys.RETURN)

        # print statements
        print("keys_username: " + keys_username)
        print("keys_email: " + keys_email)
        print("keys_password1: " + keys_password1)

        if ("Login" in driver.title):
            isValid = True
            print("TESTCASE: VALID! NEW ACCOUNT REGISTERED	✓")
            dictionary = returnDictionary(
                keys_username, keys_email, keys_password1, group)
        else:
            isValid = False
            print("TESTCASE: invalid......................")
        print()

        time.sleep(waitTime)

        return dictionary

    except:
        print("TEST FAILED TO RUN")
        time.sleep(5)
        driver.quit()


def returnDictionary(username, email, password, group):
    dictionary = {
        'username': username,
        'email': email,
        'password': password,
        'group': group,
    }
    return dictionary


def run_test_valid_register_admin(times):
    with open(filename, "r+") as file:
        data = json.load(file)

    for i in range(times):
        temp = test_register(generate_username_valid(),
                             generate_email_valid(), generate_password_valid(), True,  "admin")
        data['accounts'] .append(temp)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    file.close()
    f.close()


def run_test_valid_register_tenant(times):
    with open(filename, "r+") as file:
        data = json.load(file)

    for i in range(times):
        temp = test_register(generate_username_valid(),
                             generate_email_valid(), generate_password_valid(), True, "tenant")
        data['accounts'] .append(temp)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    file.close()
    f.close()


def run_test_INvalid_register_admin(times):
    for i in range(times):
        temp = test_register(generate_username_INvalid_chars(),
                             generate_email_valid(), generate_password_valid(), True, "admin")

        temp = test_register(generate_username_INvalid_taken(),
                             generate_email_valid(), generate_password_valid(), True, "admin")

        temp = test_register(generate_username_valid(),
                             generate_email_valid(), generate_password_valid(), False, "admin")


def run_test_INvalid_register_tenant(times):
    for i in range(times):
        temp = test_register(generate_username_INvalid_chars(),
                             generate_email_valid(), generate_password_valid(), True, "tenant")

        temp = test_register(generate_username_INvalid_taken(),
                             generate_email_valid(), generate_password_valid(), True, "tenant")

        temp = test_register(generate_username_valid(),
                             generate_email_valid(), generate_password_valid(), False, "tenant")


# run_test_valid_register_admin(3)
# run_test_valid_register_tenant(1)
run_test_INvalid_register_admin(5)
run_test_INvalid_register_tenant(2)
