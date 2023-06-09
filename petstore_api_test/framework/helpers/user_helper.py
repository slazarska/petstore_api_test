import json
import os

import requests

from petstore_api_test.framework.helpers.assert_helper import AssertHelper


class User:

    def __init__(self):
        self.url = os.getenv('URL')
        self.headers = {'Content-Type': 'application/json'}

    def get_logout_user(self):
        url = self.url + "user/logout"
        response = requests.get(url=url)
        return AssertHelper(response)

    def post_add_user(self, payload):
        url = self.url + "user"
        response = requests.post(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertHelper(response)

    def delete_user(self, username):
        url = self.url + f"user/{username}"
        response = requests.delete(url=url)
        return AssertHelper(response)
