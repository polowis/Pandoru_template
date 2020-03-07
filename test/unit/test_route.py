import os
import unittest

from app import app
class RouteTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_login_page(self):
        response = self.app.get('/login',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    

if __name__ == "__main__":
    unittest.main()