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
        elemento1=driver.find_element_by_id("user")
        elemento1.send_keys("Ludmila")
        elemento2=driver.find_element_by_id("apellidopaterno")
        elemento2.send_keys("Gonzales")
        elemento3=driver.find_element_by_id("mail")
        elemento3.send_keys("mylittlepony@gmail.com")
        #time.sleep(3)
        elemento4=driver.find_element_by_id("clave1")
        elemento4.send_keys("ludg2002")
        elemento5=driver.find_element_by_id("clave2")
        elemento5.send_keys("ludg2002")
        time.sleep(3)
        elemento6=driver.find_element_by_id("status")
        elemento6.click()
        elemento7=driver.find_element_by_link_text("Argentina")
        time.sleep(3)
        elemento7.click()
        elemento8=driver.find_element_by_id("dni")
        elemento8.send_keys("40875256")
        elemento9=driver.find_element_by_id("tipodireccion_0")
        elemento9.click()
        elemento10=driver.find_element_by_id("day")
        elemento10.click()
        elemento11=driver.find_element_by_link_text("20")
        elemento11.click()
        elemento12=driver.find_element_by_id("month")
        elemento12.click()
        elemento13=driver.find_element_by_link_text("Ago")
        elemento13.click()
        elemento14=driver.find_element_by_id("year")
        elemento14.click()
        elemento15=driver.find_element_by_link_text("2002")
        elemento15.click()
        elemento16=driver.find_element_by_id("celular")
        elemento16.send_keys("1154204499")
        elemento17=driver.find_element_by_id("checkbox")
        elemento17.click()
        elemento18=driver.find_element_by_class_name("btnVerde btnRegistroCentro")
        elemento18.click()
        time.sleep(5)


 
   

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
