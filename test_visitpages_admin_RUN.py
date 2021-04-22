import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from CONSTANTS import *

# set wait time between testcases
waitTime = 1

# NEED TO EDIT THIS BASED ON WHERE YOUR CHROMEDRIVER IS
PATH = chromeDriver_filepath

driver = webdriver.Chrome(PATH)


class TestSum(unittest.TestCase):
    def setUp(self):
        # PATH = "C:\\chromedriver.exe"
        # driver = webdriver.Chrome(PATH)
        driver.get("http://127.0.0.1:8000/logout/")
        # username
        input_username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        input_username.clear()
        input_username.send_keys(admin_username)

        # password
        input_password = driver.find_element_by_name("password")
        input_password.clear()
        input_password.send_keys(admin_password)

        # press enter
        input_password.send_keys(Keys.RETURN)

    # public pages

    def test_logout(self):
        driver.get("http://127.0.0.1:8000/logout/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_register(self):
        driver.get("http://127.0.0.1:8000/register/")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def test_registeradmin(self):
        driver.get("http://127.0.0.1:8000/register/admin")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def test_registertenant(self):
        driver.get("http://127.0.0.1:8000/register/tenant")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def test_login(self):
        driver.get("http://127.0.0.1:8000/login/")
        self.assertEqual(driver.title, "SingHealth WebApp")

    # login required

    def test_home(self):
        driver.get("http://127.0.0.1:8000/")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def test_stores(self):
        driver.get("http://127.0.0.1:8000/stores/")
        self.assertEqual(driver.title, "SingHealth WebApp - Stores")

    def test_reports(self):
        driver.get("http://127.0.0.1:8000/reports/")
        self.assertEqual(driver.title, "SingHealth WebApp - Reports")

    def test_announcements(self):
        driver.get("http://127.0.0.1:8000/announcements/")
        self.assertEqual(driver.title, "SingHealth WebApp - Announcements")

    def test_restricted(self):
        driver.get("http://127.0.0.1:8000/restricted/")
        self.assertEqual(driver.title, "Restricted Access")

    def test_send_email(self):
        driver.get("http://127.0.0.1:8000/send_email/")
        self.assertEqual(driver.title, "SingHealth WebApp - Email")

    def test_createNonFBReport_form(self):
        driver.get("http://127.0.0.1:8000/createNonFBReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Create Report")
        bodyText = driver.find_element_by_tag_name('body').text
        self.assertTrue("non-F&B" in bodyText)

    def test_createFBReport_form(self):
        driver.get("http://127.0.0.1:8000/createFBReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Create Report")
        bodyText = driver.find_element_by_tag_name('body').text
        self.assertTrue("Report — F&B" in bodyText)

    def test_createCovidReport_form(self):
        driver.get("http://127.0.0.1:8000/createCovidReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Create Report")
        bodyText = driver.find_element_by_tag_name('body').text
        self.assertTrue("Covid" in bodyText)

    def test_rectify_form(self):
        driver.get("http://127.0.0.1:8000/rectify_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Rectify Form")

    def test_chart(self):
        driver.get("http://127.0.0.1:8000/chart/")
        self.assertEqual(driver.title, "SingHealth WebApp - Accounts Ranking")

    def tearDown(self):
        time.sleep(waitTime)


if __name__ == '__main__':
    unittest.main()
