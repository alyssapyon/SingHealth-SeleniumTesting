import random
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from CONSTANTS import *
from selenium.webdriver.common.by import By

injectionUsername1a = "\\'1' or '1' = '1' /*\\'"
injectionUsername1b = '\\"1" or "1" = "1" /*\\"'

injectionPassword1a = "' OR '0'='0"
injectionPassword1b = '" OR "0"="0'

injectionUsername2a = "validuser' OR '0'='0"
injectionUsername2b = 'validuser" OR "0"="0'
# does the effect of the injection attack show?


def injectLogin(driver, username=admin_username, password=admin_password):
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

    return is_injection_protected(driver)


def is_injection_protected(driver):
    if (driver.title == "SingHealth WebApp"):
        print("ERROR! INJECTION ATTACK WORKED")
        return False
    elif (driver.title == "SingHealth WebApp - Login"):
        return True
    else:
        print("ERROR! idk where we ended up")
        print(driver.title)
        return False
