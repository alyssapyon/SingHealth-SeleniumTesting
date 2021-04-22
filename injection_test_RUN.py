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
from injection_gen import *

filename = registeredAccounts_filepath

PATH = chromeDriver_filepath
driver = webdriver.Chrome(PATH)


def testInjection():
    print("\nusername: "+injectionUsername1a)
    print("protected against injection:  " + str(
          injectLogin(driver, username=injectionUsername1a)))

    print("\nusername: "+injectionUsername1b)
    print("protected against injection  " + str(
          injectLogin(driver, username=injectionUsername1b)))

    print("\nusername: "+injectionUsername2a)
    print("protected against injection:  " + str(
          injectLogin(driver, username=injectionUsername2a)))

    print("\nusername: "+injectionUsername2b)
    print("protected against injection:  " + str(
          injectLogin(driver, username=injectionUsername2b)))

    print("\npassword: "+injectionPassword1a)
    print("protected against injection:  " + str(
          injectLogin(driver, password=injectionPassword1a)))

    print("\npassword: "+injectionPassword1b)
    print("protected against injection:  " + str(
          injectLogin(driver, password=injectionPassword1b)))


testInjection()
