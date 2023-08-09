"""
Test list
* Should return an exception when username not found
* Should return the password when the username is found
"""
import pytest

from gateways.user_repository import UserRepository
from gateways.username_not_found_exception import UsernameNotFoundException

user_repository = UserRepository()


def test_should_return_an_exception_when_username_not_found():
    with pytest.raises(UsernameNotFoundException):
        user_repository.get_password('toto')


def test_should_return_password_when_username_found():
    assert user_repository.get_password('dexter') == 'killer'
