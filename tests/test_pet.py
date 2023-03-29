import allure
from allure_commons.types import Severity

from framework.data.pet_data import get_pet_test_data
from framework.helpers.pet_helper import Pet
from framework.utils.file_path import file_pumpkin, file_teddy

pet_data = get_pet_test_data(file_teddy)
new_pet_data = get_pet_test_data(file_pumpkin)


@allure.suite('api-post')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'slazarska')
@allure.feature('Pet')
@allure.story('Adding a new pet')
def test_add_pet_with_valid_data(delete_pet):
    add_new_pet = Pet().post_add_new_pet(pet_data)
    add_new_pet.should_have_status_code(200)
    add_new_pet.should_have_body_field("id", pet_data["id"])
    add_new_pet.should_have_body_field("category", pet_data["category"])
    add_new_pet.should_have_body_field("name", pet_data["name"])
    add_new_pet.should_have_body_field("status", pet_data["status"])


@allure.suite('api-post')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'slazarska')
@allure.feature('Pet')
@allure.story('Find the pet')
def test_find_pet_by_id(add_pet):
    get_pet_by_id = Pet().get_pet_by_id(pet_data["id"])
    get_pet_by_id.should_have_status_code(200)
    get_pet_by_id.should_have_body_field("name", pet_data["name"])
    get_pet_by_id.should_have_body_field("status", pet_data["status"])


@allure.suite("api-delete")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'slazarska')
@allure.feature('Pet')
@allure.story('Deleting the pet')
def test_delete_pet(add_pet):
    delete_pet = Pet().delete_pet(pet_data)
    delete_pet.should_have_status_code(200)
    delete_pet.should_have_body_field("code", 200)
    delete_pet.should_have_body_field("message", str(pet_data["id"]))


@allure.suite("api-put")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'slazarska')
@allure.feature('Pet')
@allure.story('Changing the pet')
def test_update_existing_pet(add_pet, delete_pet):
    update_existing_pet = Pet().put_existing_pet(new_pet_data)
    update_existing_pet.should_have_status_code(200)
    update_existing_pet.should_have_body_field("name", new_pet_data["name"])
    update_existing_pet.should_have_body_field("status", new_pet_data["status"])

    get_pet_by_id = Pet().get_pet_by_id(new_pet_data["id"])
    get_pet_by_id.should_have_status_code(200)
    get_pet_by_id.should_have_body_field("name", new_pet_data["name"])
    get_pet_by_id.should_have_body_field("status", new_pet_data["status"])
