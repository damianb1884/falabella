import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class registro (unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path=r"C:\driver Chrome\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
