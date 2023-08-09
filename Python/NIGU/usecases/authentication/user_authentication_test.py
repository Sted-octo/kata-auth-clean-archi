"""
Test list
* Doit retourner une exception quand le mot de passe est vide
* Doit retourner une exception quand le nom est vide
* Doit retourner une exception si l'utilisateur n'existe pas en base (nom)
* Doit retourner une exception si l'utilisateur a entrer un mauvais mot de passe
"""
import pytest
from unittest.mock import patch


from entities.user import User
from gateways.username_not_found_exception import UsernameNotFoundException
from usecases.authentication.bad_password_exception import BadPasswordException
from usecases.authentication.password_empty_exception import PasswordEmptyException
from usecases.authentication.user_authentication import UserAuthentication
from usecases.authentication.username_empty_exception import UsernameEmptyException


def test_should_return_an_exception_when_password_empty():
    user = User('toto', '')
    with pytest.raises(PasswordEmptyException):
        UserAuthentication.login(user)


def test_should_return_an_exception_when_name_empty():
    user = User('', '0000')
    with pytest.raises(UsernameEmptyException):
        UserAuthentication.login(user)


def test_should_return_an_exception_if_username_not_found():
    user = User('toto', '0000')
    with pytest.raises(UsernameNotFoundException):
        UserAuthentication.login(user)


def test_should_return_an_exception_if_bad_password():
    user = User('dexter', '0000')
    with pytest.raises(BadPasswordException):
        UserAuthentication.login(user)


def test_should_return_a_32_chars_token_if_good_credentials():
    user = User('dexter', 'killer')
    with patch('random.choice', return_value="a"):
        assert UserAuthentication.login(user) == "a"*32
