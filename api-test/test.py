from main import create_folder, delete_folder
import unittest


class TestYandexApi(unittest.TestCase):

    def test_error_create_folder(self):
        self.assertEqual(create_folder('file_successful'), 201)


    def test_successful_create_folder(self):
        self.assertEqual(create_folder('file_successful'), 409)


if __name__ == '__main__':
    unittest.main()