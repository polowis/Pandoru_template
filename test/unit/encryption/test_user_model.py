from app.model.user import User
import unittest

class UserTest(unittest.TestCase):
    def test_password(self):
        user = User()
        user.username ="polowis" 
        user.email=' exmaple@gmail.com'
        user.password = 'irunaonlinepolowis'

if __name__ == '__main__':
    unittest.main()
