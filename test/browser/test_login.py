import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test.browser import getDriver
from app import app
from app.model.user import User

app_url = app.config.get('APP_URL')
app_port = app.config.get('APP_PORT')
app_domain = f'{app_url}:{app_port}'

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        print('Testing login page..')
        os.system('flask db:fresh')
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        os.system('flask db:fresh')
        self.driver.quit()

    def test_login(self):

        #self.driver.implicitly_wait(10)
        self.driver.get(f'{app_domain}/login')
        
        user = User()
        user.username = 'Example'
        user.email = 'example@gmail.com'
        user.password = 'examplepassword'
        user.user_id = 32
        user.save()

        email = self.driver.find_element_by_name('user_email')
        password = self.driver.find_element_by_name('pass')
        

        email.send_keys('example@gmail.com')
        password.send_keys('examplepassword')
        submit_button = self.driver.find_element_by_id('submit_button')
        submit_button.send_keys(Keys.ENTER)

        current_url = self.driver.current_url
        self.assertEqual(current_url, f'{app_domain}/dashboard')

if __name__ == '__main__':
    unittest.main()