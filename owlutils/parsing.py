"""Common parsing utils used across owl company web apps"""


def safeint(value):
    """safely converts value to integer or none"""
    try:
        return int(float(value))
    except ValueError:
        return None


def safeintorzero(value):
    """safely converts value to integer or 0"""
    try:
        return int(value)
    except ValueError:
        return 0


def safeintorbignumber(value):
    """safely converts value to integer or 10M"""
    try:
        return int(value)
    except ValueError:
        return 10000000


def safefloat(value):
    """safely converts value to float or none"""
    try:
        return float(value)
    except ValueError:
        return None
