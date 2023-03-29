import json

import requests

from framework.helpers.assert_helper import AssertHelper


class Pet:

    def __init__(self):
        self.url = "https://petstore.swagger.io/v2/"
        self.headers = {'Content-Type': 'application/json'}

    def get_pet_by_id(self, pet_id):
        url = self.url + f"pet/{pet_id}"
        response = requests.get(url=url)
        return AssertHelper(response)

    def get_pets_by_status(self, params):
        url = self.url + "pet/findByStatus"
        response = requests.get(url=url, params=params)
        return AssertHelper(response)

    def post_add_new_pet(self, payload):
        url = self.url + "pet"
        response = requests.post(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertHelper(response)

    def post_existing_pet_with_form_data(self, pet_id, data):
        url = self.url + f"pet/{pet_id}"
        response = requests.post(url=url, data=data)
        return AssertHelper(response)

    def put_existing_pet(self, payload):
        url = self.url + "pet"
        response = requests.put(url=url, data=json.dumps(payload), headers=self.headers)
        return AssertHelper(response)

    def delete_pet(self, pet_id):
        url = self.url + f"pet/{pet_id}"
        response = requests.delete(url=url)
        return AssertHelper(response)
