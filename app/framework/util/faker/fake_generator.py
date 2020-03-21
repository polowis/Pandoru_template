import forgery_py
from app import db

from app.model.user import User
from app.framework.util.faker.faker import Faker
faker = Faker()
class FakerGenerator(object):
    def __init__(self):
        db.drop_all()
        db.create_all()
    
    def generate_fake_users(self, count):
        for i in range(count):
            User(
                email=faker.email_address,
                username=faker.username,
                password="correcthorsebatterystaple",
            ).save()