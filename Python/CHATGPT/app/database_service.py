from app.core.entities import User

class DatabaseService:
    def __init__(self):
        self.users = {
            "dexter": User("dexter", "killer")
        }

    def get_user_by_name(self, name):
        return self.users.get(name)
