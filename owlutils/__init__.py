"""Common utils used across owl company web apps"""

__version__ = "0.1.0"


def safeint(value):
    try:
        return int(value)
    except:
        return None
