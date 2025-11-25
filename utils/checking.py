"""Methods for checking the responses of our queries"""
import json


class Checking():
    """Method for checking status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, 'Error, Status code does not match'
        print(f"Successfully! Status code = {result.status_code}")

    """Method for checking the presence of required fields in a request response"""
    @staticmethod
    def check_json_fields(result, expected_value):
        """Method for checking the presence of fields in a request response"""
        fields = json.loads(result.text)
        assert list(fields) == expected_value, 'Error, Field list does not match'
        # print(list(fields))
        print("All fields are present")

    """Method for checking the values of required fields in a request response"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(check_info)
        print(f"{field_name} right!")

    """Method for checking the values of required fields in a request response using a search for a specific word"""
    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f"Word {search_word} present")
