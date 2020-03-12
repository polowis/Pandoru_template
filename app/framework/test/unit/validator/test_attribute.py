import unittest
from app.framework.requests.validate_request import *
from app.framework.util.faker import Faker

faker = Faker()

class RouteTest(unittest.TestCase):
    def test_alphanumeric_validator(self):
        self.assertEqual(Validator.validate_alphanumeric('<>"fsja', 'test'), False)
        self.assertEqual(Validator.validate_alphanumeric(faker.alphanumeric, 'test'), True)
    

    def test_alpha_validator(self):
        self.assertEqual(Validator.validate_alpha(faker.alpha, 'test'), True)


if __name__ == "__main__":
    unittest.main()
