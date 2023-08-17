from app.database_service import DatabaseService
from app.interfaces.token_service import TokenService
from app.core.use_cases import AuthenticateUseCase
from app.interfaces.controllers import AuthController

def configure_dependencies():
    database_service = DatabaseService()
    auth_use_case = AuthenticateUseCase(database_service)
    token_service = TokenService()
    auth_controller = AuthController(auth_use_case, token_service)
    return auth_controller

auth_controller = configure_dependencies()
