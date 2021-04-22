import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import json

from gen_username_valid import generate_username_valid
from gen_email_valid import generate_email_valid
from gen_password_valid import generate_password_valid
from CONSTANTS import *
from xss_gen import *

filename = registeredAccounts_filepath

PATH = chromeDriver_filepath
driver = webdriver.Chrome(PATH)

############################################
# supporing functions below


def register(username=generate_username_valid(), email=generate_email_valid(), password=generate_password_valid()):
    driver.get("http://127.0.0.1:8000/logout/")
    driver.get("http://127.0.0.1:8000/register/admin/")
    # username
    input_username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    input_username.clear()
    input_username.send_keys(username)

    # email
    input_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    input_email.clear()
    input_email.send_keys(email)

    # password1
    input_password1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password1"))
    )
    input_password1.clear()
    input_password1.send_keys(password)

    # password2
    input_password2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password2"))
    )
    input_password2.clear()
    input_password2.send_keys(password)

    # press enter
    input_password2.send_keys(Keys.RETURN)
    return


def login(username=admin_username, password=admin_password):
    driver.get("http://127.0.0.1:8000/logout/")
    # username
    input_username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    input_username.clear()
    input_username.send_keys(username)

    # password
    input_password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    input_password.clear()
    input_password.send_keys(password)

    # press enter
    input_password.send_keys(Keys.RETURN)
    return


def createReport(link, reportNo=random.randint(1, 20), score=random.randint(1, 20)):
    login()
    driver.get(link)
    storefield = Select(driver.find_element_by_name("store"))
    storefield.select_by_index(1)
    reportfield = driver.find_element_by_name('report_number')
    reportfield.clear()
    reportfield.send_keys(reportNo)
    scorefield = driver.find_element_by_name('score')
    scorefield.clear()
    scorefield.send_keys(score)
    submit_button = driver.find_element_by_name('submit')
    submit_button.click()
    return


def sendEmail(driver, email="alyssapyon@gmail.com", subject="testsubject", message="testmessage"):
    login()
    driver.get("http://127.0.0.1:8000/send_email/")
    # email
    emailfield = driver.find_element_by_id('id_email')
    emailfield.clear()
    emailfield.send_keys(email)

    # subject
    subjectfield = driver.find_element_by_id('id_subject')
    subjectfield.clear()
    subjectfield.send_keys(subject)

    # message
    emailfield = driver.find_element_by_id('id_message')
    emailfield.clear()
    emailfield.send_keys(message)

    submit_button = driver.find_element_by_name('Submit')
    submit_button.click()
    return
############################################


# register


def test_register_username():
    register(username=xssTestString)
    return no_xss_popup(driver)


def test_register_email():
    register(email=xssTestString)
    return no_xss_popup(driver)


def test_register_password():
    register(password=xssTestString)
    return no_xss_popup(driver)

# login


def test_login_username():
    login(username=xssTestString)
    return no_xss_popup(driver)


def test_login_password():
    login(password=xssTestString)
    return no_xss_popup(driver)

# create FB report


def test_FBreport_no():
    createReport("http://127.0.0.1:8000/createFBReport_form/",
                 reportNo=xssTestString)
    return no_xss_popup(driver)


def test_FBreport_score():
    createReport("http://127.0.0.1:8000/createFBReport_form/",
                 score=xssTestString)
    return no_xss_popup(driver)

# create Non FB report


def test_nonFBreport_no():
    createReport("http://127.0.0.1:8000/createNonFBReport_form/",
                 reportNo=xssTestString)
    return no_xss_popup(driver)


def test_nonFBreport_score():
    createReport("http://127.0.0.1:8000/createNonFBReport_form/",
                 score=xssTestString)
    return no_xss_popup(driver)


# create covid report

def test_covidreport_no():
    createReport("http://127.0.0.1:8000/createCovidReport_form/",
                 reportNo=xssTestString)
    return no_xss_popup(driver)


def test_covidreport_score():
    createReport("http://127.0.0.1:8000/createCovidReport_form/",
                 score=xssTestString)
    return no_xss_popup(driver)

# send email


def test_sendEmail_email():
    sendEmail(driver, email=xssTestString)
    return no_xss_popup(driver)


def test_sendEmail_subject():
    sendEmail(driver, subject=xssTestString)
    return no_xss_popup(driver)


def test_sendEmail_message():
    sendEmail(driver, message=xssTestString)
    return no_xss_popup(driver)


############################################
# TESTING DONE HERE
waittime = 1

# print("test_register_username: " + str(test_register_username()))
# time.sleep(waittime)
# print("test_register_email: " + str(test_register_email()))
# time.sleep(waittime)
# print("test_register_password: " + str(test_register_password()))
# time.sleep(waittime)

# print("test_login_username: " + str(test_login_username()))
# time.sleep(waittime)
# print("test_login_password: " + str(test_login_password()))
# time.sleep(waittime)

print("test_FBreport_no: " + str(test_FBreport_no()))
time.sleep(waittime)
print("test_FBreport_no: " + str(test_FBreport_no()))
time.sleep(waittime)
print("test_nonFBreport_no: " + str(test_nonFBreport_no()))
time.sleep(waittime)
print("test_nonFBreport_score: " + str(test_nonFBreport_score()))
time.sleep(waittime)
print("test_covidreport_no: " + str(test_covidreport_no()))
time.sleep(waittime)
print("test_covidreport_score: " + str(test_covidreport_score()))
time.sleep(waittime)

print("test_sendEmail_email: " + str(test_sendEmail_email()))
time.sleep(waittime)
print("test_sendEmail_subject: " + str(test_sendEmail_subject()))
time.sleep(waittime)
print("test_sendEmail_message: " + str(test_sendEmail_message()))
time.sleep(waittime)
