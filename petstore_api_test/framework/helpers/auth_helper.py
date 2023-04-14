import os

import requests

from petstore_api_test.framework.helpers.assert_helper import AssertHelper
from dotenv import load_dotenv

load_dotenv()


class Authentication:

    def __init__(self):
        self.url = os.getenv('URL')
        self.headers = {'Content-Type': 'application/json'}

    def get_login_user(self, params):
        url = self.url + 'user/login'
        response = requests.get(url=url, params=params)
        return AssertHelper(response)
