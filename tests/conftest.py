import os

import pytest
from dotenv import load_dotenv

from petstore_api_test.framework.data.pet_data import get_pet_test_data
from petstore_api_test.framework.data.user_data import TestUserData
from petstore_api_test.framework.helpers.auth_helper import Authentication
from petstore_api_test.framework.helpers.pet_helper import Pet
from petstore_api_test.framework.helpers.user_helper import User
from petstore_api_test.framework.utils.base_session import BaseSession
from petstore_api_test.framework.utils.file import teddy

load_dotenv()
url = os.getenv('URL')

created_user = {"id": TestUserData.USER_ID,
                "username": TestUserData.USERNAME,
                "firstName": TestUserData.FIRSTNAME,
                "lastName": TestUserData.LASTNAME,
                "email": TestUserData.EMAIL,
                "password": TestUserData.PASSWORD,
                "phone": TestUserData.PHONE,
                "userStatus": TestUserData.USER_STATUS}

created_pet = get_pet_test_data(teddy)


@pytest.fixture(scope='function', autouse=True)
def session():
    return BaseSession(url)


@pytest.fixture()
def login_user():
    valid_creds = {
        'username': os.getenv('USERNAME'),
        'password': os.getenv('PASSWORD'),
    }
    Authentication().get_login_user(valid_creds)


@pytest.fixture()
def create_user():
    User().post_add_user(created_user)


@pytest.fixture()
def delete_user():
    yield
    User().delete_user(created_user["username"])


@pytest.fixture()
def add_pet():
    Pet().post_add_new_pet(created_pet)


@pytest.fixture()
def delete_pet():
    yield
    Pet().delete_pet(created_pet["id"])
