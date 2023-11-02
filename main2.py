import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import main2

# class LogInPage(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get('https://ccb.elevatenp.org/enroll/')
#         # Waits for web elements to load first
#         self.driver.implicitly_wait(10)

#     def test_login(self):
#         password = self.driver.find_element(By.ID, 'password_protected_pass')
#         password.send_keys('cbb')
#         submit_button = self.driver.find_element(By.ID, "wp-submit")
#         submit_button.click()
#         assert True

#     def tearDown(self):
#         self.driver.close()

class ConctactFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ccb.elevatenp.org/enroll/')
        self.driver.implicitly_wait(20)

    # Logs into testing environment
    def test_login(self):
        password = self.driver.find_element(By.ID, 'password_protected_pass')
        password.send_keys('ccb')
        submit_button = self.driver.find_element(By.ID, "wp-submit")
        submit_button.click()

        # Wait for the next page to load 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tfa_FirstName'))
        )
        
        assert True
    
    def test_step1(self):
        # Form elements
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
        # self.driver.close()
        pass

if __name__ == '__main__':
    unittest.main()