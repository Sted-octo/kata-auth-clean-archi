from gateways.username_not_found_exception import UsernameNotFoundException


class UserRepository:
    def __init__(self):
        self.users = {
            "dexter": "killer"
        }

    def get_password(self, username: str):
        try :
            return self.users[username]
        except KeyError:
            raise UsernameNotFoundException
