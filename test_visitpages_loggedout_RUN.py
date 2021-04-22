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
        driver.get("http://127.0.0.1:8000/logout/")

    # public pages

    def test_logout(self):
        driver.get("http://127.0.0.1:8000/logout/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_register(self):
        driver.get("http://127.0.0.1:8000/register/")
        self.assertEqual(driver.title, "SingHealth WebApp - Register")

    def test_registeradmin(self):
        driver.get("http://127.0.0.1:8000/register/admin")
        self.assertEqual(driver.title, "SingHealth WebApp - Register Admin")

    def test_registertenant(self):
        driver.get("http://127.0.0.1:8000/register/tenant")
        self.assertEqual(driver.title, "SingHealth WebApp - Register Tenant")

    def test_login(self):
        driver.get("http://127.0.0.1:8000/login/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    # login required

    def test_home(self):
        driver.get("http://127.0.0.1:8000/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_stores(self):
        driver.get("http://127.0.0.1:8000/stores/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_reports(self):
        driver.get("http://127.0.0.1:8000/reports/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_announcements(self):
        driver.get("http://127.0.0.1:8000/announcements/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_restricted(self):
        driver.get("http://127.0.0.1:8000/restricted/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_send_email(self):
        driver.get("http://127.0.0.1:8000/send_email/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_createNonFBReport_form(self):
        driver.get("http://127.0.0.1:8000/createNonFBReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_createFBReport_form(self):
        driver.get("http://127.0.0.1:8000/createFBReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_createCovidReport_form(self):
        driver.get("http://127.0.0.1:8000/createCovidReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_rectify_form(self):
        driver.get("http://127.0.0.1:8000/rectify_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def tearDown(self):
        time.sleep(waitTime)


if __name__ == '__main__':
    unittest.main()
