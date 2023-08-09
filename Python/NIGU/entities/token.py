import string
import random

TOKEN_SIZE = 32


class Token:

    @staticmethod
    def generate_token():
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(TOKEN_SIZE))
