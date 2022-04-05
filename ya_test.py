import os
import unittest
import ya_api


class YaApiTest(unittest.TestCase):
    TEST_DIRECTORY = "test_dir"

    def setUp(self) -> None:
        ya_token = os.getenv("YA_TOKEN")
        self.ya_api = ya_api.YaApi(ya_token)

    def test_create_directory(self):
        http_code, res_json = self.ya_api.create_directory(self.TEST_DIRECTORY)
        self.assertEqual(http_code, 201)

    def tearDown(self) -> None:
        self.ya_api.delete_directory(self.TEST_DIRECTORY)

