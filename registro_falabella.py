#from optparse import Option
#from select import select
#from tkinter.tix import Select
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
        time.sleep(1)
        elemento4=driver.find_element_by_id("clave1")
        elemento4.send_keys("ludg2002")
        elemento5=driver.find_element_by_id("clave2")
        elemento5.send_keys("ludg2002")
        time.sleep(1)

        
        seleccionar2=Select(driver.find_element_by_id("status"))
        seleccionar2.select_by_value("362")
        
        time.sleep(1)
        
        elemento8=driver.find_element_by_id("dni")
        elemento8.send_keys("40875256")
        elemento9=driver.find_element_by_id("tipodireccion_0")
        elemento9.click()
        time.sleep(1)
        elemento10=Select(driver.find_element_by_id("day"))
        elemento10.select_by_value("20")
        time.sleep(1)
        elemento12=Select(driver.find_element_by_id("month"))
        elemento12.select_by_value("08")
        time.sleep(1)
        elemento14=Select(driver.find_element_by_id("year"))
        elemento14.select_by_value("2002")
        time.sleep(1)
        elemento16=driver.find_element_by_id("celular")
        elemento16.send_keys("1154204499")
        elemento17=driver.find_element_by_id("agreelegaleId")
        elemento17.click()
        elemento18=driver.find_element_by_id("boton_Ar")
        elemento18.click()
        time.sleep(1)
        


 
   

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
