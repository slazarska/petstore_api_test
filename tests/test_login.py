import json
import random
from datetime import datetime

import pytest
import requests
from dateutil import parser
from pytz import utc

from framework.data.user_data import TestUserData

base_url = 'https://petstore.swagger.io/v2/user'

json_for_new_user = {"id": TestUserData.USER_ID,
                        "username": TestUserData.USERNAME,
                        "firstName": TestUserData.FIRSTNAME,
                        "lastName": TestUserData.LASTNAME,
                        "email": TestUserData.EMAIL,
                        "password": TestUserData.PASSWORD,
                        "phone": TestUserData.PHONE,
                        "userStatus": TestUserData.USER_STATUS}

valid_creds = {
    'username': json_for_new_user['username'],
    'password': json_for_new_user['password'],
}

empty_creds = {
    'username': " ",
    'password': " ",
}

invalid_creds = {
    'username': f'InvalidUsername{random.randint(333, 999)}',
    'password': f'InvalidPassword{random.randint(999, 3333)}',
}


def test_create_user():
    response = requests.post(
        base_url,
        data=json.dumps(json_for_new_user),
        headers={'Content-Type': 'application/json'},
    )
    response_body = response.json()
    assert response.status_code == 200
    assert int(response_body['message']) == json_for_new_user['id'], 'unexpected user id in the response'


@pytest.mark.dependency(depends=['test_create_user'])
def test_login():
    response = requests.get(f'{base_url}/login', params=valid_creds)

    x_expires_after = response.headers['X-Expires-After']
    x_rate_limit = response.headers['X-Rate-Limit']
    now = datetime.utcnow().replace(tzinfo=utc)

    assert int(response.status_code) == 200
    assert 'logged in user session:' in response.json()['message'], 'no expected substring in the message attribute'
    assert now <= parser.parse(x_expires_after), 'token expire time should not be earlier than the current time'
    assert int(x_rate_limit) == 5000, 'unexpected value of request rate limit'


@pytest.mark.dependency(depends=['test_login'])
def test_logout():
    response = requests.get(f'{base_url}/logout')

    assert response.status_code == 200
    assert response.json()['message'] == 'ok', 'unexpected "message" attribute value'


def test_login_with_no_credentials():
    response = requests.get(f'{base_url}/login', params=empty_creds)

    assert response.status_code == 400


def test_login_with_invalid_credentials():
    response = requests.get(f'{base_url}/login', params=invalid_creds)

    assert response.status_code == 400

