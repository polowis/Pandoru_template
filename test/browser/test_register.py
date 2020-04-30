import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from app.model.user import User
from app import app, db
import os
from test.browser import getDriver

app_url = app.config.get('APP_URL')
app_port = app.config.get('APP_PORT')
app_domain = f'{app_url}:{app_port}'

class TestRegistrationPage(unittest.TestCase):
    def setUp(self):
        print('Testing Register page...')
        self.driver = webdriver.Chrome()
        os.system('flask db:fresh')
    
    def tearDown(self):
        os.system('flask db:fresh')
        self.driver.quit()
        
    
    def test_register_form(self):
        self.driver.get(f'{app_domain}/register')
        
        username = self.driver.find_element_by_name('username')
        email = self.driver.find_element_by_name('email')
        password = self.driver.find_element_by_name('password')
        password_confirmation = self.driver.find_element_by_name('password_confirmation')

        username.send_keys('example')
        email.send_keys('example@gmail.com')
        password.send_keys('irunaonlinepolowis')
        password_confirmation.send_keys('exampleofsuperlongpassword')

        submit_button = self.driver.find_element_by_id('register')
        submit_button.send_keys(Keys.ENTER)

        current_url = self.driver.current_url
        self.assertEqual(current_url, f'{app_domain}')
        

if __name__ == '__main__':
    unittest.main() 
