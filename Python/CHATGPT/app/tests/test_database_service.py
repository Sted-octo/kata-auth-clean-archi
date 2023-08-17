# auth_api/app/tests/test_database_service.py
import unittest
from app.database_service import DatabaseService

class TestDatabaseService(unittest.TestCase):
    def setUp(self):
        self.database_service = DatabaseService()

    def test_get_user_by_name_existing(self):
        user = self.database_service.get_user_by_name("dertex")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "dertex")
        self.assertEqual(user.password, "killer")

    def test_get_user_by_name_non_existing(self):
        user = self.database_service.get_user_by_name("nonexistent")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()