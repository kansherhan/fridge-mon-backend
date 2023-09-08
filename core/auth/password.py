import bcrypt


class Password:
    @classmethod
    def correct(cls, password: str, hash: str):
        return bcrypt.checkpw(password.encode(), hash.encode())

    @classmethod
    def hash(cls, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
