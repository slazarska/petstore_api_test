import random

from petstore_api_test.framework.data import generator


class TestUserData:

    USER_ID = random.randint(10000, 100000)
    USERNAME = generator.generate_random_string()
    FIRSTNAME = generator.generate_firstname()
    LASTNAME = generator.generate_lastname()
    EMAIL = generator.generate_random_email()
    PASSWORD = generator.generate_random_password()
    PHONE = generator.generate_random_phone_number()
    USER_STATUS = random.randint(1, 3)

