import random
import string

class TokenService:
    @staticmethod
    def generate_token():
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
