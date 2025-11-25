import json
import allure
from requests import Response
from utils.checking import Checking
from utils.api import Google_maps_api

"""Creating, editing, and deleting a new location"""
@allure.epic("Test creat place")
class Test_create_place():
    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("Метод Post")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        fields = json.loads(result_post.text)
        Checking.check_json_value(result_post, 'status', 'OK')


        print("Метод Get Post")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')


        print("Метод Put")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_fields(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')


        print("Метод Get Put")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get,
                                   ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                    'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Метод Delete")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_fields(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Метод Get Delete")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_fields(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')


        print("Testing of creating, editing and deleting a new location was successfully completed!!!")
