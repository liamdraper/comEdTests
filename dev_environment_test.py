import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ConctactFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ccb.elevatenp.org/enroll/')
        # Wait for initial element to load
        self.driver.implicitly_wait(5)

    def test_form(self):
        password = self.driver.find_element(By.ID, 'password_protected_pass')
        log_in_button = self.driver.find_element(By.ID, "wp-submit")

        password.send_keys('ccb')
        log_in_button.click()

        # Wait for the next page to load 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tfa_FirstName'))
        )

        print('test')

        # Now not typing keys in
        # Identifying page elements within variables
        first_name = self.driver.find_element(By.ID, 'tfa_FirstName')
        last_name = self.driver.find_element(By.ID, 'tfa_LastName')
        email = self.driver.find_element(By.ID, 'tfa_Email')
        confirm_email = self.driver.find_element(By.ID, 'tfa_ConfirmEmail')
        next_page_button1 = self.driver.find_element(By.ID, 'wfPageNextId1')

        # Fill in form
        first_name.send_keys("John")
        last_name.send_keys("Doe")
        email.send_keys("johndoe@example.com")
        confirm_email.send_keys("johndoe@example.com")
        next_page_button1.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tfa_7945020484363'))
        )

        phone = self.driver.find_element(By.ID, 'tfa_7945020484363')
        street_address = self.driver.find_element(By.ID, 'tfa_StreetAddress')
        city = self.driver.find_element(By.ID, 'tfa_City')
        state = self.driver.find_element(By.ID, 'tfa_State')
        zip = self.driver.find_element(By.ID, 'tfa_Zip')
        # Also need to test the "Copy from Mailing Address" button
        service_address = self.driver.find_element(By.ID, 'tfa_7945020484414')
        service_city = self.driver.find_element(By.ID, 'tfa_7945020484415')
        service_state = self.driver.find_element(By.ID, 'tfa_7945020484416')
        service_zip = self.driver.find_element(By.ID, 'tfa_7945020484417')
        next_page_button2 = self.driver.find_element(By.ID, 'wfPageNextId2')

        phone.send_keys('7732694037')
        street_address.send_keys('322 S Green St #300')
        city.send_keys('Chicago')
        state.send_keys('IL')
        zip.send_keys('60607')
        service_address.send_keys('322 S Green St #300')
        service_city.send_keys('Chicago')
        service_state.send_keys('IL')
        service_zip.send_keys('60607')
        next_page_button2.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tfa_AccountNumbernod'))
        )

        account_number = self.driver.find_element(By.ID, 'tfa_AccountNumbernod')
        next_page_button3 = self.driver.find_element(By.ID, 'wfPageNextId3')

        account_number.send_keys('1234567890')
        next_page_button3.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tfa_7945020484360'))
        )

        option1 = self.driver.find_element(By.ID, 'tfa_7945020484522')
        option2 = self.driver.find_element(By.ID, 'tfa_7945020484395')
        drop_down_menu = self.driver.find_element(By.ID, 'tfa_7945020484398')
        next_page_button4 = self.driver.find_element(By.ID, 'wfPageNextId4')

        option1.click()
        option2.click()
        select = Select(drop_down_menu)
        select.select_by_visible_text('Acura NSX')
        next_page_button4.click() 
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tfa_7945020484355-HTML'))
        )

        checkbox = self.driver.find_element(By.ID, 'tfa_7945020484355-HTML')
        alert_email = self.driver.find_element(By.ID, 'tfa_7945020484423')
        next_page_button5 = self.driver.find_elements(By.ID, 'wfPageNextId5')

        checkbox.click()
        alert_email.send_keys('johndoe@example.com')
        next_page_button5.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tfa_referalQuestion-L'))
        )

        no_referral = self.driver.find_element(By.ID, 'tfa_referalQuestionNo')
        community_meeting = self.driver.find_element(By.ID, 'tfa_CommunityMeeting')
        next_page_button6 = self.driver.find_element(By.ID, 'wfPageNextId6')

        no_referral.click()
        community_meeting.click()
        next_page_button6.click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()