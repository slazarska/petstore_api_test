import json


def get_pet_test_data(file_name):
    with open(file_name) as pet_json:
        pet_data = json.load(pet_json)
        return pet_data
