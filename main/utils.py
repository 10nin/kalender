# coding=utf-8

# Generic utility functions.
import re
from calendar import Calendar
from datetime import datetime
from hashlib import sha3_512
from uuid import uuid4
from dateutil.relativedelta import relativedelta


def normalize_data(s: str) -> str:
    """Normalize unicode string
    :arg s: target string
    :return normalized string
    """
    from unicodedata import normalize
    return normalize('NFKC', s)


def get_hashval(passwd: str, salt: str) -> str:
    hs = sha3_512()
    p = passwd.encode('utf-8') + salt.encode('utf-8')
    hs.update(p)
    return hs.hexdigest().upper()


def get_unique_str(length: int) -> str:
    return uuid4().hex[:length]


def valid_date(d: str) -> bool:
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


def validate_date_full(d: str) -> bool:
    """
    validate date format of d
    :param d: target datetime it expect YYYYMMDD
    :return:
    """
    if len(d) != len('YYYYMMDD'):
        return False
    try:
        datetime.strptime(d[:4], '%Y')
    except ValueError:
        return False
    re_month = r'(0[1-9]|1[0-2])'
    if re.match(re_month, d[4:6]) is None:
        return False
    re_day = r'(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
    if re.match(re_day, d[6:8]) is None:
        return False
    # all validation was passed.
    return True


def generate_days(year: int, month: int):
    # week is start by sunday
    cal = Calendar(firstweekday=6)
    return cal.monthdayscalendar(year, month)


def split_request_date(request_date: str) -> (int, int):
    """
    split request_date to year and month
    :param request_date: split target date on 'YYYYMM' formatted string.
    :return: (year, month) tuple.
    """
    year = int(request_date[:4])
    month = int(request_date[4:6])
    return year, month


def split_request_date_full(request_date: str) -> (int, int, int):
    """
    split request_date to year and month
    :param request_date: split target date on 'YYYYMM' formatted string.
    :return: (year, month) tuple.
    """
    year = int(request_date[:4])
    month = int(request_date[4:6])
    day = int(request_date[6:8])
    return year, month, day


def get_current_date() -> str:
    """
    return current date formatted YYYYMM
    :return: current year and month
    """
    return datetime.strftime(datetime.now(), '%Y%m')


def get_current_date_full() -> str:
    """
    return current date formatted YYYYMMDD
    :return: current year and month
    """
    return datetime.strftime(datetime.now(), '%Y%m%d')


def get_prev_and_next_month(year: int, month: int) -> (str, str):
    dt = datetime(year=year, month=month, day=1)
    prev_month = dt - relativedelta(months=1)
    next_month = dt + relativedelta(months=1)
    return prev_month.strftime('%Y%m'), next_month.strftime('%Y%m')
