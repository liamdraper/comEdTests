import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
service = Service(executable_path="/Users/liamdraper/Documents/VSCode/comEdTests/chromedriver")

class ConctactFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://hourlypricing.comed.com/enroll/')

    def test_step1(self):
        # Form elements
        self.driver.implicitly_wait(10)
        first_name = self.driver.find_element(By.ID, 'tfa_FirstName')
        last_name = self.driver.find_element(By.ID, 'tfa_LastName')
        email = self.driver.find_element(By.ID, 'tfa_Email')
        confirm_email = self.driver.find_element(By.ID, 'tfa_ConfirmEmail')

        # Fill in form
        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys("johndoe@example.com")
        confirm_email.send_keys("johndoe@example.com")

        submit_button = self.driver.find_element(By.ID, "wfPageNextId1")
        submit_button.click()

        assert True
    
    def test_step2(self):
        self.driver.implicitly_wait(10)
        phone = self.driver.find_element(By.ID, 'tfa_7945020484363')
        street_address = self.driver.find_element(By.ID, '#tfa_StreetAddress')
        city = self.driver.find_element(By.ID, '#tfa_City')
        state = self.driver.find_element(By.ID, '#tfa_State')
        zip = self.driver.find_element(By.ID, '#tfa_Zip')
        # Also need to test the "Copy from Mailing Address" button
        service_address = self.driver.find_element(By.ID, '#tfa_7945020484414')
        service_city = self.driver.find_element(By.ID, '#tfa_7945020484415')
        service_state = self.driver.find_element(By.ID, '#tfa_7945020484416')
        service_zip = self.driver.find_element(By.ID, '#tfa_7945020484417')

        phone.send_keys('7732694037')
        street_address.send_keys('322 S Green St #300')
        city.send_keys('Chicago')
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()