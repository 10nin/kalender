# coding=utf-8

# Generic utility functions.
import re
from hashlib import sha3_512
from uuid import uuid4

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
    return hs.hexdigest().upper()

def get_unique_str(length: int) -> str:
    return uuid4().hex[:length]

def valid_date(d):
    """date validator.
    if date(d) is invalid format
       or it not in the scope at 2018/01 to 2019/12 then
       return the False <means invalid>."""

    valid_month = r'(0[123456789]|1[0-2])'
    # validation pass through
    if len(d) == 0:
        return False
    # invalid request date
    if len(d) != 6:  # validate data length
        return False
    if d[:4] != '2018' and d[:4] != '2019':  # validate year
        return False
    if re.match(valid_month, d[4:6]) is None:  # validate month
        return False
    return True
