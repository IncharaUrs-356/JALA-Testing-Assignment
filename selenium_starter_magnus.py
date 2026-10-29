"""
Starter Selenium tests for Magnus.
Install: pip install selenium
Use only with authorized training credentials. Update locators after inspecting the live page.
"""
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APP_URL = os.getenv("MAGNUS_URL", "http://magnus.jalatechnologies.com/")
USERNAME = os.getenv("MAGNUS_USERNAME", "")
PASSWORD = os.getenv("MAGNUS_PASSWORD", "")

class MagnusSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 15)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_page_loads(self):
        self.driver.get(APP_URL)
        self.assertTrue(self.driver.title or self.driver.find_elements(By.TAG_NAME, "body"))

    @unittest.skipUnless(USERNAME and PASSWORD, "Set MAGNUS_USERNAME and MAGNUS_PASSWORD environment variables")
    def test_login_with_training_account(self):
        self.driver.get(APP_URL)
        # TODO: Inspect the actual login page and replace these placeholder locators.
        username = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # TODO: Assert a stable authenticated-page element after inspecting the real UI.
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.assertTrue(self.driver.find_elements(By.TAG_NAME, "body"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
