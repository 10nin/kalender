# coding=utf-8

# Generic utility functions.
from hashlib import sha3_512


def normalize_data(s: str):
    """Normalize unicode string
    :arg s: target string
    :return normalized string
    """
    from unicodedata import normalize
    return normalize('NFKC', s)

def get_hashval(passwd: str, salt: str):
    hs = sha3_512()
    p = passwd.encode('utf-8') + salt.encode('utf-8')
    hs.update(p)
    return hs.hexdigest()
