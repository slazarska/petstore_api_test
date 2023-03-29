import requests

from framework.helpers.assert_helper import AssertHelper


class Authentication:

    def __init__(self):
        self.url = 'https://petstore.swagger.io/v2/'
        self.headers = {'Content-Type': 'application/json'}

    def get_login_user(self, params):
        url = self.url + 'user/login'
        response = requests.get(url=url, params=params)
        return AssertHelper(response)
