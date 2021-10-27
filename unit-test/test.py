from main import get_doc_owner_name, add_new_doc, delete_doc
import unittest


class TestProgram(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('11-2'), 'Геннадий Покемонов')

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('226', 'pass', 'Nikita', 7), 7)

    def test_delete_doc(self):
        self.assertTrue(delete_doc('2207 876234'))


if __name__ == '__main__':
    unittest.main()
