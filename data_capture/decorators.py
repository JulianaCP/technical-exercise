"""
Decorators
----------

Check arguments: accepts_integer_type is a decorator that
checks that all of the receives arguments for each of the stats
methods are integers.).

Between range: accepts_between_range will check
if the sent number.
"""
from typing import Callable, List


def accepts_integer_type(func: Callable) -> Callable:
    """Checks that each of the received arguments in
    the decorated function are integers.

    :param Callable func: Function to be decorated.
    """
    def wrapper(cls, *args: List[int]):
        for argument in args:
            if not isinstance(argument, int):
                raise ValueError("Argument(s) does not match <class 'int'>.")
        return func(cls, *args)
    return wrapper


def accepts_in_range(min_number: int, max_number: int):
    """Checks that each of the received arguments are
    between a given range.

    :param int min_number: Minimum number.
    :param int max_number: Maximum number.
    """
    def decorator(func: Callable):
        def wrapper(cls, *args):
            if not all([min_number <= arg <= max_number for arg in args]):
                raise ValueError(f"Numbers must be between: {min_number} "
                                 f"and {max_number}")
            return func(cls, *args)
        return wrapper
    return decorator
