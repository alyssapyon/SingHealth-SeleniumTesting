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

filename = registeredAccounts_filepath

PATH = chromeDriver_filepath
driver = webdriver.Chrome(PATH)

waittime = 1

############################################
# supporing functions below


def login():
    driver.get("http://127.0.0.1:8000/logout/")
    # username
    input_username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    input_username.clear()
    input_username.send_keys(admin_username)

    # password
    input_password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    input_password.clear()
    input_password.send_keys(admin_password)

    # press enter
    input_password.send_keys(Keys.RETURN)
    return


def createRandomReport(link):
    login()
    driver.get(link)

    # store
    storefield = Select(driver.find_element_by_name("store"))
    storeoptions = storefield.options
    storeoptions_text = []
    for i in range(1, len(storeoptions)):
        storeoptions_text.append(storeoptions[i].text)

    choice = random.randint(1, len(storeoptions_text))
    # print(storeoptions_text[choice])
    storefield.select_by_index(choice)

    # report no
    reportfield = driver.find_element_by_name('report_number')
    reportfield.clear()
    reportNo = random.randint(1, 20)
    reportfield.send_keys(reportNo)

    # compliance
    checkboxes = driver.find_elements_by_xpath("//input[@name='compliance']")
    for each_checkbox in checkboxes:
        tickOptions = [True, False]
        toTick = random.choice(tickOptions)

        if toTick:
            if not each_checkbox.is_selected():  # just to be sure that you make check, but not uncheck
                driver.execute_script('arguments[0].click()', each_checkbox)

    # score
    scorefield = driver.find_element_by_name('score')
    scorefield.clear()
    score = random.randint(0, 20)
    scorefield.send_keys(score)

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()
    return [storeoptions_text[choice-1], reportNo, score]


def checkIfReportCreated():
    if driver.title == "SingHealth WebApp":
        return True
    elif driver.title == "SingHealth WebApp - Create Report":
        return False
    else:
        print("ERROR")
        return False


def checkReportData(data):
    driver.get("http://127.0.0.1:8000/reports/")
    bodyText = driver.find_element_by_tag_name('body').text
    for i in data:
        if str(i) not in bodyText:
            return False
    return True

############################################


def test_createFBreport():
    print("TEST: creating a new FB report")
    data = createRandomReport("http://127.0.0.1:8000/createFBReport_form/")
    if checkIfReportCreated():
        print("report was created!")
        print(".............................. PASS")
    else:
        print("ERROR: report was not created")

    print(data)
    print("")


def test_createnonFBreport():
    print("TEST: creating a new non FB report")
    data = createRandomReport("http://127.0.0.1:8000/createNonFBReport_form/")
    if checkIfReportCreated():
        print("report was created!")
    else:
        print("ERROR: report was not created")
        print(data)
    if checkReportData(data):
        print("data is shown correctly")
        print(".............................. PASS")
    else:
        print("ERROR: data was not shown correctly")
        print(data)
    print("")
    pass


def test_createcovidreport():
    print("TEST: creating a new covid report")
    data = createRandomReport("http://127.0.0.1:8000/createCovidReport_form/")
    if checkIfReportCreated():
        print("report was created!")
        print(".............................. PASS")
    else:
        print("ERROR: report was not created")
        print(data)
    print("")
    pass


def testReports(fb=1, nonfb=1, covid=1):
    for i in range(fb):
        test_createFBreport()
        time.sleep(waittime)

    for i in range(nonfb):
        test_createnonFBreport()
        time.sleep(waittime)

    for i in range(covid):
        test_createcovidreport()
        time.sleep(waittime)
############################################
# TESTING DONE HERE


testReports()
