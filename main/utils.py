# coding=utf-8

# Generic utility functions.
import re
from calendar import Calendar
from datetime import datetime
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
    """
    validate date format of d
    :param d: target datetime it expect YYYYMM
    :return:
    """
    if len(d) != len('YYYYMM'):
        return False
    try:
        datetime.strptime(d[:4], '%Y')
    except ValueError:
        return False
    re_month = r'(0[1-9]|1[0-2])'
    if re.match(re_month, d[4:6]) is None:
        return False
    # all validation was passed.
    return True


def generate_days(year, month):
    # week is start by sunday
    cal = Calendar(firstweekday=6)
    ret = list()
    for c in cal.itermonthdates(year, month):
        if c.month == month:
            ret.append(c.day)
        else:
            ret.append("")
    return ret
