from app import app
import unittest
import vowel_counter


class TestVowelCount(unittest.TestCase):
    
    #set up and destroying of mock webserver
    def setUp(self):
        self.app = app.test_client()

    def destroy(self):
        pass

    #basic unit test for function
    def test_vowel_count(self):
        self.assertEqual(vowel_counter.count_vowels('maisy'),2)

    def test_request_with_valid_parameters(self):
        response = self.app.get('/?x=test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), '{"String": "test", "answer": "1", "Status Code": "200", "Errors": "false"}')

    def test_request_with_no_parameters(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode("utf-8"), '{"String": "No Text Entered", "answer": 0, "Status Code": "404", "Errors": "true"}')

    def test_request_with_wrong_parameters_all_digits(self):
        response = self.app.get('/?x=12345')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode("utf-8"), '{"String": "Please enter character strings, not numbers", "answer": 0, "Status Code": "404", "Errors": "true"}')

    def test_request_with_incorrect_route(self):
        response = self.app.get('/wrong')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode("utf-8"), '{"String": "No Text Entered", "answer": 0, "Status Code": "404", "Errors": "true"}')

   



   

if __name__== 'main':
    unittest.main()