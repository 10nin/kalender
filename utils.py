# coding=utf-8

# Generic utility functions.


def normalize_data(s: str):
    """Normalize unicode string
    :arg s: target string
    :return normalized string
    """
    from unicodedata import normalize
    return normalize('NFKC', s)
