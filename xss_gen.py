import random
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


xssTestString = "<script>alert('...haha, you have been XSS-ed...')</script>"

# does the effect of the xss attack show?


def no_xss_popup(driver):
    try:
        alert_obj = driver.switch_to.alert
        msg = alert_obj.text
        alert_obj.accept()
        print("alert found")

        if "haha" in msg:
            print("VULNERABLE TO XSS ATTACKS")
            return False
        else:
            return True
    except:
        return True


def is_xss_protected(driver, type, identifier):
    inputfield = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((type, identifier))
    )

    inputfield.clear()
    inputfield.send_keys(xssTestString)
    inputfield.send_keys(Keys.RETURN)

    no_xss_popup(driver)

# supporting functions
