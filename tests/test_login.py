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


@allure.label('owner', 'slazarska')
@allure.feature('User')
class TestLogin:
    @allure.severity(Severity.BLOCKER)
    @allure.story('Authorization')
    def test_login(self):
        with allure.step('Login with valid credentials'):
            login_user = Authentication().get_login_user(valid_creds)

        with allure.step('Check login is successful'):
            login_user.should_have_status_code(200)
            login_user.should_have_body_field("code", 200)
            login_user.does_str_in_value("message", "logged in user session:")

    @allure.severity(Severity.CRITICAL)
    @allure.story('Authorization')
    def test_logout(self, login_user):
        with allure.step('Logout'):
            logout_user = User().get_logout_user()

        with allure.step('Check logout is successful'):
            logout_user.should_have_status_code(200)
            logout_user.should_have_body_field("code", 200)
            logout_user.should_have_body_field("message", "ok")

    @allure.severity(Severity.NORMAL)
    @allure.story('Authorization')
    def test_login_with_no_credentials(self):
        with allure.step('Login with empty credentials'):
            login_user = Authentication().get_login_user(empty_creds)
        with allure.step('Check login with empty credentials is failed'):
            login_user.should_have_status_code(400)
            login_user.should_have_body_field("code", 400)

    @allure.severity(Severity.NORMAL)
    @allure.story('Authorization')
    def test_login_with_invalid_credentials(self):
        with allure.step('Login with invalid credentials'):
            login_user = Authentication().get_login_user(invalid_creds)
        with allure.step('Check login with invalid credentials is failed'):
            login_user.should_have_status_code(400)
            login_user.should_have_body_field("code", 400)

    @allure.severity(Severity.CRITICAL)
    @allure.story('Create a new user')
    def test_create_user(self, delete_user):
        with allure.step('Add a new user'):
            create_user = User().post_add_user(created_user)
        with allure.step('Check the new user is successfully created'):
            create_user.should_have_status_code(200)
            create_user.should_have_body_field("code", 200)
            create_user.should_have_body_field("message", str(created_user["id"]))

    @allure.severity(Severity.NORMAL)
    @allure.story('Deleting the user')
    def test_delete_user(self, create_user):
        with allure.step('Delete the user'):
            delete_user = User().delete_user(created_user["username"])
        with allure.step('Check the user is successfully deleted'):
            delete_user.should_have_status_code(200)
            delete_user.should_have_body_field("code", 200)
            delete_user.should_have_body_field("message", str(created_user["username"]))
