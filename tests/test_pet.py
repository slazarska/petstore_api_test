import allure
from allure_commons.types import Severity

from petstore_api_test.framework.data.pet_data import get_pet_test_data
from petstore_api_test.framework.helpers.pet_helper import Pet
from petstore_api_test.framework.utils.file_path import pumpkin, teddy

pet_data = get_pet_test_data(teddy)
new_pet_data = get_pet_test_data(pumpkin)


@allure.label('owner', 'slazarska')
@allure.feature('Pet')
class TestPet:
    @allure.severity(Severity.CRITICAL)
    @allure.story('Adding a new pet')
    def test_add_pet_with_valid_data(self, delete_pet):
        with allure.step('Add a new pet'):
            add_new_pet = Pet().post_add_new_pet(pet_data)

        with allure.step('Check the new pet is successfully created'):
            add_new_pet.should_have_status_code(200)
            add_new_pet.should_have_body_field("id", pet_data["id"])
            add_new_pet.should_have_body_field("category", pet_data["category"])
            add_new_pet.should_have_body_field("name", pet_data["name"])
            add_new_pet.should_have_body_field("status", pet_data["status"])

    @allure.severity(Severity.NORMAL)
    @allure.story('Find the pet')
    def test_find_pet_by_id(self, add_pet):
        with allure.step('Find the pet by id'):
            get_pet_by_id = Pet().get_pet_by_id(pet_data["id"])

        with allure.step('Check the pet is successfully found'):
            get_pet_by_id.should_have_status_code(200)
            get_pet_by_id.should_have_body_field("name", pet_data["name"])
            get_pet_by_id.should_have_body_field("status", pet_data["status"])

    @allure.severity(Severity.NORMAL)
    @allure.story('Deleting the pet')
    def test_delete_pet(self, add_pet):
        with allure.step('Delete the pet'):
            delete_pet = Pet().delete_pet(pet_data)

        with allure.step('Check the pet is successfully deleted'):
            delete_pet.should_have_status_code(200)
            delete_pet.should_have_body_field("code", 200)
            delete_pet.should_have_body_field("message", str(pet_data["id"]))

    @allure.severity(Severity.NORMAL)
    @allure.story('Changing the pet')
    def test_update_existing_pet(self, add_pet, delete_pet):
        with allure.step('Update the existing pets data'):
            update_existing_pet = Pet().put_existing_pet(new_pet_data)

        with allure.step('Check the pets data is successfully updated'):
            update_existing_pet.should_have_status_code(200)
            update_existing_pet.should_have_body_field("name", new_pet_data["name"])
            update_existing_pet.should_have_body_field("status", new_pet_data["status"])

        with allure.step('Find the pet by id'):
            get_pet_by_id = Pet().get_pet_by_id(new_pet_data["id"])

        with allure.step('Check the new pets data'):
            get_pet_by_id.should_have_body_field("name", new_pet_data["name"])
            get_pet_by_id.should_have_body_field("status", new_pet_data["status"])
