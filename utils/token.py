def generate_token(length: int):
    from binascii import hexlify
    from os import urandom

    return hexlify(urandom(length / 2)).decode()
