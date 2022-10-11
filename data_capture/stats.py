"""
Stats class

This class provides methods for calculating statistics of data, including
less, between, and greater.

==================  ==================================================
Function            Description
==================  ==================================================
less                Numbers lower than X.
between             Numbers between than X and Y.
greater             Numbers greater than X.
==================  ==================================================

Numbers lower than X:

>> capture = DataCapture()
>> capture.add(3)
>> capture.add(9)
>> capture.add(3)
>> capture.add(4)
>> capture.add(6)
>> stats = capture.build_stats()
>> stats.less(4)
2


Numbers between X and Y:

>> capture = DataCapture()
>> capture.add(3)
>> capture.add(9)
>> capture.add(3)
>> capture.add(4)
>> capture.add(6)
>> stats = capture.build_stats()
>> stats.between(3, 6)
4


Numbers greater than X:

>> capture = DataCapture()
>> capture.add(3)
>> capture.add(9)
>> capture.add(3)
>> capture.add(4)
>> capture.add(6)
>> stats = capture.build_stats()
>> stats.between(3, 6)
2
"""
from typing import List

from data_capture.decorators import accepts_integer_type


class Stats:
    """The Stats class contains functionality to compute
    some basic statistics on a list of numbers (including
    less, between, and greater).
    """
    def __init__(self, sorted_numbers: list, mappings: dict):
        """
        :param list sorted_numbers: List that contains all the
        numbers that were added to the data capture class.
        :param dict mappings: Mappings of the min and max index of
        each number.
        """
        self._sorted_numbers = sorted_numbers
        self._mappings = mappings
        self._len_numbers = len(sorted_numbers)
        self._first_number = sorted_numbers[0]
        self._last_number = sorted_numbers[-1]

    @property
    def sorted_numbers(self) -> List:
        """Returns the list of sorted numbers."""
        return self._sorted_numbers

    @accepts_integer_type
    def less(self, number: int) -> int:
        """This method will return an integer presenting
        how many numbers in the sorted list are lower than
        the given number.

        :param int number: Stats number to check.

        :returns: Integer representing how many numbers
        in the list are lower than the given number.
        :rtype: int.
        """
        if self._first_number > number:
            return 0

        if self._last_number < number:
            return self._len_numbers

        return self._mappings[number]["min_index"]

    @accepts_integer_type
    def greater(self, number: int) -> int:
        """his method will return an integer presenting
        how many numbers in sorted list are greater than
        the given number.

        :param int number: Stats number.

        :returns: Integer representing how many numbers
        in the sorted list are greater than the given number.
        :rtype: int.
        """
        if self._first_number > number:
            return self._len_numbers

        if self._last_number < number:
            return 0

        return self._len_numbers - self._mappings[number]["max_index"] - 1

    @accepts_integer_type
    def between(self, min_number: int, max_number: int) -> int:
        """This method will return an integer presenting
        how many numbers in the sorted list are between
        a given range [a, b].

        :param int min_number: Minimum number to check.
        :param int max_number: Maximum number to check.

        :returns: Integer representing how many numbers
        in the sorted list are between the given range.
        :rtype: int.
        """
        if min_number > max_number:
            min_number, max_number = max_number, min_number

        greater_counter = self.greater(max_number)
        less_counter = self.less(min_number)
        return self._len_numbers - greater_counter - less_counter
