from datetime import datetime

from core.hash import Hash

from apps.auth.models import EmployeeToken as Token


class TokenManager:
    @classmethod
    def generate_token(cls, length: int) -> str:
        return Hash.generate_hash(length)

    @classmethod
    def check_token_life_cycle(cls, token: Token, token_lifetime: int) -> bool:
        total_seconds = (datetime.now() - token.created_at).total_seconds()

        return total_seconds < token_lifetime
