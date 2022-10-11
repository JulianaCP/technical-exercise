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


Data Capture class

This class provides methods for handling a number
collection and the  generation of stats from it.

==================  ==================================================
Function            Description
==================  ==================================================
add                 Adds a number to a collection.
build_stats         Generates a Stats class instance to use later for
                    calculating statistics of data.
==================  ==================================================

Add a number:

>> capture = DataCapture()
>> capture.add(3)


Generate a Stats class:

>> capture = DataCapture()
>> stats = capture.build_stats()
"""
from typing import List, Dict

from data_capture.decorators import accepts_in_range, accepts_integer_type
from data_capture.stats import Stats


class DataCapture:
    """The DataCapture object accepts numbers and returns an object for querying
    statistics about the inputs. By default the class will support
    additions of numbers between 0 and 1000 (inclusive).
    """
    def __init__(self, max_numbers=1000):
        self._max_numbers = max_numbers
        self._numbers_existence = [0] * (max_numbers + 1)

    @property
    def numbers_existence(self) -> List:
        """Returns the list of numbers."""
        return self._numbers_existence

    @accepts_integer_type
    @accepts_in_range(0, 1000)
    def add(self, number: int) -> None:
        """Adds a number to a list (numbers that
        will be used to compute the statistics).

        :param int number: Number to be added to the
        full list of possible numbers.
        """
        self._numbers_existence[number] += 1

    def _trimmed_and_sort_numbers(self) -> List:
        """Creates a list that contains all the
        numbers that were added to the list (using
        the created list that contains all the
        possible numbers existence -> len = max_numbers)
        It will trimmed the full list of numbers creating
        a new list with just the numbers that were
        added. (It will preserve the order of the numbers
        returning a sorted list of numbers).

        :returns: Trimmed and sorted list of numbers.
        :rtype: List[int]
        """
        trimmed_sorted_numbers = []
        for number, counter in enumerate(self._numbers_existence):
            if counter != 0:
                trimmed_sorted_numbers.extend([number] * counter)
        return trimmed_sorted_numbers

    @staticmethod
    def generate_mappings(sorted_numbers: list) -> Dict:
        """Generates a mappings of the min and max index of each value
        to later use to counter the number of numbers according to
        the less, greater and between methods.

        :param list sorted_numbers:  Sorted list of numbers.

        :returns: Number mappings  dictionary (min and max index
        mapped for each number). Dictionary will be used by
        the Stats class to compute some basic statistics on a
        collection of small positive integers.
        :rtype: Dict
        """
        mappings = {}
        inverted_numbers = sorted_numbers[::-1]
        previous_min_index = None
        previous_max_index = None
        # iterate over all possible numbers between the minimum number
        # and the list and th  maximum added  number  in the list
        # (to map all possible numbers in the range).
        for number in range(sorted_numbers[0], sorted_numbers[-1] + 1, 1):
            if number in sorted_numbers:
                # extract min index and max index of each number.
                min_index = sorted_numbers.index(number)
                max_index = len(sorted_numbers) - inverted_numbers.index(number) - 1
                mappings[number] = {"min_index": min_index, "max_index": max_index}
                previous_min_index = mappings[number]["max_index"] + 1
                previous_max_index = mappings[number]["min_index"]
            else:
                # fill out intermediate mappings of numbers that are not in the list.
                mappings[number] = {"min_index": previous_min_index,
                                    "max_index": previous_max_index}
        return mappings

    def build_stats(self) -> Stats:
        """Sorts the list of numbers and returns an object for querying
        statistics about the inputs. The returned object supports
        querying how many numbers in the collection are less than a value, greater
        than a value, or within a range.

        :returns: Creates a stats class instance with the current
        state of the list of numbers and generates some mappings from
        it to compute some basic statistics on a collection of
        small positive integers.
        :rtype: Stats
        """
        sorted_numbers = self._trimmed_and_sort_numbers()
        mappings = self.generate_mappings(sorted_numbers)
        return Stats(sorted_numbers, mappings)
