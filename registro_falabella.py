import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class registro (unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path=r"C:\driver Chrome\chromedriver.exe")

    def test_1falabella(self):
        driver=self.driver
        driver.get("https://secure.falabella.com.ar/falabella-ar/myaccount/register.jsp?CJSESSIONID=6ovKyMizQXwmMcGtNej45EEo.node3205&CURRENCYCODE=ARS&fromPage=&DPSLogout=true")
        time.sleep(3)
        driver.find_element_by_id("user")
        driver.find_element_by_id("apellidopaterno")
        driver.find_element_by_id("mail")
        driver.find_element_by_id("clave1")
        driver.find_element_by_id("clave2")
   
 
   

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
