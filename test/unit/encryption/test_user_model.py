from app.model.user import User
import unittest

class UserTest(unittest.TestCase):
    def test_password(self):
        user = User()
        user.username ="polowis" 
        user.email=' exmaple@gmail.com'
        user.password = 'irunaonlinepolowis'
        self.assertEqual(user.has_correct_password('irunaonlinepolowis'), True)
        self.assertEqual(user.has_correct_password('sdfsa'), False)

if __name__ == '__main__':
    unittest.main()