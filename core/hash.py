from binascii import hexlify
from os import urandom


class Hash:
    @classmethod
    def generate_hash(cls, length: int) -> str:
        return hexlify(urandom(length)).decode()[:length]
