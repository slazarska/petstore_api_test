import pytest

from framework.data.pet_data import get_pet_test_data
from framework.utils.base_session import BaseSession
from framework.helpers.auth_helper import Authentication
from framework.helpers.user_helper import User
from framework.helpers.pet_helper import Pet
from framework.data.user_data import TestUserData
from framework.utils.file_path import file_teddy

base_url = 'https://petstore.swagger.io/v2/'

json_for_new_user = {"id": TestUserData.USER_ID,
                     "username": TestUserData.USERNAME,
                     "firstName": TestUserData.FIRSTNAME,
                     "lastName": TestUserData.LASTNAME,
                     "email": TestUserData.EMAIL,
                     "password": TestUserData.PASSWORD,
                     "phone": TestUserData.PHONE,
                     "userStatus": TestUserData.USER_STATUS}

created_pet = get_pet_test_data(file_teddy)


@pytest.fixture(scope='function', autouse=True)
def just_session():
    return BaseSession('https://petstore.swagger.io/v2/')


@pytest.fixture()
def login_user():
    valid_creds = {
        'username': "new_scamander",
        'password': "22tatFbacb",
    }
    login_user = Authentication().get_login_user(valid_creds)
    login_user.should_have_status_code(200)
    login_user.should_have_body_field("code", 200)
    login_user.does_str_in_value("message", "logged in user session:")


@pytest.fixture()
def create_user():
    create_user = User().post_add_user(json_for_new_user)
    create_user.should_have_status_code(200)


@pytest.fixture()
def delete_user():
    yield
    delete_user = User().delete_user(json_for_new_user["username"])
    delete_user.should_have_status_code(200)


@pytest.fixture()
def add_pet():
    add_new_pet = Pet().post_add_new_pet(created_pet)
    add_new_pet.should_have_status_code(200)


@pytest.fixture()
def delete_pet():
    yield
    delete_pet = Pet().delete_pet(created_pet["id"])
    delete_pet.should_have_status_code(200)
