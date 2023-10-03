import warnings
from functools import wraps


def deprecated(reason):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(f"Deprecated function: {func.__name__}. Reason: {reason}", DeprecationWarning)
            return func(*args, **kwargs)

        return wrapper

    return decorator
