from app.core.entities import User

class AuthenticateUseCase:
    def __init__(self, database_service):
        self.database_service = database_service

    def authenticate(self, name, password):
        user = self.database_service.get_user_by_name(name)
        if user and user.password == password:
            return True
        return False