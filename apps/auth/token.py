from binascii import hexlify
from os import urandom
from datetime import datetime

from .models import EmployeeToken as Token


class TokenManager:
    @classmethod
    def generate_token(cls, length: int) -> str:
        return hexlify(urandom(length)).decode()[:length]

    @classmethod
    def check_token_lifetime(cls, token: Token, token_lifetime: int) -> bool:
        total_seconds = (datetime.now() - token.updated_at).total_seconds()
        print(total_seconds, token_lifetime)

        return total_seconds < token_lifetime
