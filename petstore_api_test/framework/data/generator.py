import random
import string

from faker import Faker

fake = Faker()


def generate_firstname():
    return fake.first_name()


def generate_lastname():
    return fake.last_name()


def generate_random_string(length: int = 5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_random_email():
    return f"{generate_random_string()}.@gmail.com"


def generate_random_password():
    return f"{generate_random_string()}{random.randint(0, 1000)})"


def generate_random_phone_number():
    area_code = str(random.randint(100, 999))
    exchange_code = str(random.randint(100, 999))
    subscriber_number = str(random.randint(1000, 9999))
    return f"{area_code}-{exchange_code}-{subscriber_number}"
