import unittest

from fastapi.testclient import TestClient

from main import app, generate_random_number, get_hello_message

client = TestClient(app)


class TestMain(unittest.TestCase):
    def test_get_hello_message_returns_expected_text(self):
        self.assertEqual(get_hello_message(), {"message": "Hello World"})

    def test_generate_random_number_returns_integer(self):
        number = generate_random_number()

        self.assertIsInstance(number, int)

    def test_generate_random_number_is_between_1_and_10(self):
        number = generate_random_number()

        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 10)

    def test_hello_route_returns_status_code_200(self):
        response = client.get("/hello")

        self.assertEqual(response.status_code, 200)

    def test_hello_route_returns_expected_body(self):
        response = client.get("/hello")

        self.assertEqual(response.json(), {"message": "Hello World"})

    def test_random_int_route_returns_expected_fields(self):
        response = client.get("/random-int")
        body = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(body["teste"])
        self.assertIsInstance(body["random_int"], int)
        self.assertGreaterEqual(body["random_int"], 1)
        self.assertLessEqual(body["random_int"], 10)
