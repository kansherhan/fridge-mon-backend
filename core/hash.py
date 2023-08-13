from binascii import hexlify
from os import urandom


def generate_hash(length: int) -> str:
    return hexlify(urandom(length)).decode()[:length]
