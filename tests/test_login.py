import random

import allure
from allure_commons.types import Severity

from petstore_api_test.framework.data.user_data import TestUserData
from petstore_api_test.framework.helpers.auth_helper import Authentication
from petstore_api_test.framework.helpers.user_helper import User

created_user = {"id": TestUserData.USER_ID,
                "username": TestUserData.USERNAME,
                "firstName": TestUserData.FIRSTNAME,
                "lastName": TestUserData.LASTNAME,
                "email": TestUserData.EMAIL,
                "password": TestUserData.PASSWORD,
                "phone": TestUserData.PHONE,
                "userStatus": TestUserData.USER_STATUS}

valid_creds = {
    'username': "newt_scamander",
    'password': "22tatFbacb",
}

empty_creds = {
    'username': " ",
    'password': " ",
}

invalid_creds = {
    'username': f'InvalidUsername{random.randint(333, 999)}',
    'password': f'InvalidPassword{random.randint(999, 3333)}',
}


@allure.suite("api-get")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'slazarska')
@allure.feature('User')
@allure.story('Authorization')
def test_login():
    login_user = Authentication().get_login_user(valid_creds)
    login_user.should_have_status_code(200)
    login_user.should_have_body_field("code", 200)
    login_user.does_str_in_value("message", "logged in user session:")


@allure.suite("api-get")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'slazarska')
@allure.feature('User')
@allure.story('Authorization')
def test_logout(login_user):
    logout_user = User().get_logout_user()
    logout_user.should_have_status_code(200)
    logout_user.should_have_body_field("code", 200)
    logout_user.should_have_body_field("message", "ok")


@allure.suite("api-get")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'slazarska')
@allure.feature('User')
@allure.story('Authorization')
def test_login_with_no_credentials():
    login_user = Authentication().get_login_user(empty_creds)
    login_user.should_have_status_code(400)
    login_user.should_have_body_field("code", 400)


@allure.suite("api-get")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'slazarska')
@allure.feature('User')
@allure.story('Authorization')
def test_login_with_invalid_credentials():
    login_user = Authentication().get_login_user(invalid_creds)
    login_user.should_have_status_code(400)
    login_user.should_have_body_field("code", 400)


@allure.suite("api-post")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'slazarska')
@allure.feature('User')
@allure.story('Create a new user')
def test_create_user(delete_user):
    create_user = User().post_add_user(created_user)
    create_user.should_have_status_code(200)
    create_user.should_have_body_field("code", 200)
    create_user.should_have_body_field("message", str(created_user["id"]))


@allure.suite("api-delete")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'slazarska')
@allure.feature('User')
@allure.story('Deleting the user')
def test_delete_user(create_user):
    delete_user = User().delete_user(created_user["username"])
    delete_user.should_have_status_code(200)
    delete_user.should_have_body_field("code", 200)
    delete_user.should_have_body_field("message", str(created_user["username"]))
