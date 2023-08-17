from app.database_service import DatabaseService
from app.interfaces.token_service import TokenService

class DependencyContainer:
    def __init__(self):
        self.database_service = DatabaseService()
        self.token_service = TokenService()

dependency_container = DependencyContainer()
