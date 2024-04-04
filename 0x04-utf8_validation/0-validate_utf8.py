#!/usr/bin/python3
"""Validating UTF8 integers
"""


def validUTF8(data):
    """method to check of an integer list are UTF-8
    """
    _skip_int = 0
    n = len(data)
    for i in range(n):
        if _skip_int > 0:
            _skip_int -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            tof = False
            return tof
        elif data[i] <= 0x7f:
            _skip_int = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if n - i >= span:
                _next = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(_next):
                    tof = False
                    return tof
                _skip_int = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if n - i >= span:
                _next = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(_next):
                    tof = False
                    return tof
                _skip_int = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if n - i >= span:
                _next = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(_next):
                    tof = False
                    return tof
                _skip_int = span - 1
            else:
                return False
        else:
            return False
    return True
