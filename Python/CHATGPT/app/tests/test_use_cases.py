import unittest
from unittest.mock import Mock

from app.core.entities import User
from app.core.use_cases import AuthenticateUseCase
from app.database_service import DatabaseService

class TestAuthenticateUseCase(unittest.TestCase):
    def setUp(self):
        self.database_service = Mock(spec=DatabaseService)
        self.authenticate_use_case = AuthenticateUseCase(self.database_service)

    def test_authenticate_valid_user(self):
        self.database_service.get_user_by_name.return_value = User("dertex", "killer")
        result = self.authenticate_use_case.authenticate("dertex", "killer")
        self.assertTrue(result)

    def test_authenticate_invalid_user(self):
        self.database_service.get_user_by_name.return_value = None
        result = self.authenticate_use_case.authenticate("nonexistent", "password")
        self.assertFalse(result)

    def test_authenticate_wrong_password(self):
        self.database_service.get_user_by_name.return_value = User("dertex", "killer")
        result = self.authenticate_use_case.authenticate("dertex", "wrong_password")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
