from entities.token import Token
from entities.user import User
from gateways.user_repository import UserRepository
from usecases.authentication.bad_password_exception import BadPasswordException
from usecases.authentication.password_empty_exception import PasswordEmptyException
from usecases.authentication.username_empty_exception import UsernameEmptyException


class UserAuthentication:
    @staticmethod
    def login(user: User):
        if user.name == '':
            raise UsernameEmptyException
        elif user.password == '':
            raise PasswordEmptyException
        else:
            user_repository = UserRepository()
            if user_repository.get_password(user.name) == user.password:
                return Token.generate_token()
            raise BadPasswordException

