import unittest
from unittest.mock import Mock
from app.core.use_cases import AuthenticateUseCase
from run import database_service

class TestAuthenticateUseCase(unittest.TestCase):
    def setUp(self):
        self.authenticate_use_case = AuthenticateUseCase(database_service)

    def test_authenticate_valid_user(self):
        database_service.get_user_by_name.return_value = {"name": "dertex", "password": "killer"}
        result = self.authenticate_use_case.authenticate("dertex", "killer")
        self.assertTrue(result)

    def test_authenticate_invalid_user(self):
        database_service.get_user_by_name.return_value = None
        result = self.authenticate_use_case.authenticate("nonexistent", "password")
        self.assertFalse(result)

    def test_authenticate_wrong_password(self):
        database_service.get_user_by_name.return_value = {"name": "dertex", "password": "killer"}
        result = self.authenticate_use_case.authenticate("dertex", "wrong_password")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
