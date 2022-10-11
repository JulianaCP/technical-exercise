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


Decorators
----------

A single decorator is defined: check_arguments is a decorator that
checks that all of the receives arguments for each of the stats
methods are integers.
"""


def check_arguments(func):
    """Checks that each of the receive arguments are integers.
    (Note: max number of arguments set to 3. This was set to 3
    arguments instead of setting N number of arguments (with *args)
    because it will required to iterate over the list of args, but
    im trying to avoid that since will increase the big O complexity
    of the decorator to O(n), so in regards of kipping the O(1)
    complexity, the decorator was set to 3. [in case you want to
    accept N number, you just need to set *args and create a for to
    assert each of the arguments]).
    """
    def func_wrapper(cls, first_arg, second_arg=None, third_arg=None):
        valid_type = int
        invalid_msg = "Argument(s) does not match <class 'int'>."
        assert isinstance(third_arg, valid_type) or not third_arg, invalid_msg
        assert isinstance(second_arg, valid_type) or not second_arg, invalid_msg
        assert isinstance(first_arg, valid_type), invalid_msg

        # send the second parameter if arguments was sent, if not, send just the first one.
        if third_arg:
            return func(cls, first_arg, second_arg, third_arg)
        elif second_arg:
            return func(cls, first_arg, second_arg)
        else:
            return func(cls, first_arg)

    return func_wrapper


class Stats:
    def __init__(self, sorted_numbers, mappings):
        self._sorted_numbers = sorted_numbers
        self._mappings = mappings
        self._counter_numbers = len(sorted_numbers)
        self._first_number = sorted_numbers[0]
        self._last_number = sorted_numbers[-1]

    def less(self, number):
        """Checks if the sent number is lower than X (being X
        the number to check that will represent an element
        in the list).

        :param int number: Stats number.
        """
        if self._first_number > number:
            return 0

        if self._last_number < number:
            return self._counter_numbers

        return self._mappings[number]["min_index"]

    def greater(self, number):
        """Checks if the sent number is greater than X (being X
        the number to check that will represent an element
        in the list).

        :param int number: Stats number.
        """
        if self._first_number > number:
            return self._counter_numbers

        if self._last_number < number:
            return 0

        return self._counter_numbers - self._mappings[number]["max_index"] - 1

    def between(self, min_number, max_number):
        """Checks if the sent number is between X and Y (being X
        the minimum number to check and Y the maximum number to
        check.

        :param int min_number: Minimum number to check.
        :param int max_number: Maximum number to check. .
        """
        greater_counter = self.greater(max_number)
        less_counter = self.less(min_number)
        return self._counter_numbers - greater_counter - less_counter


class DataCapture:
    """The DataCapture object accepts numbers and returns an object for querying
    statistics about the inputs. Specifically, the returned object supports
    querying how many numbers in the collection are less than a value, greater
    than a value, or within a range.
    """
    def __init__(self, max_numbers=1000):
        self._max_numbers = max_numbers
        self._numbers_existence = [0] * (max_numbers + 1)

    @property
    def numbers_existence(self):
        """Returns the private attribute numbers existence, that contains
        the list with numbers.
        """
        return self._numbers_existence

    def add(self, number):
        """Adds a number to the numbers list (available numbers to
        manipulate and generate the stats).
        """
        self._numbers_existence[number] += 1

    def _trimmed_and_sort_numbers(self):
        trimmed_sorted_numbers = []
        for number, counter in enumerate(self._numbers_existence):
            if counter != 0:
                trimmed_sorted_numbers.extend([number] * counter)
        return trimmed_sorted_numbers

    @staticmethod
    def generate_mappings(sorted_numbers):
        """Generates a mappings of the min and max index of each value
        to later use to counter the number of numbers according to
        the less, greater and between methods.

        :param list sorted_numbers:  Sorted list of numbers.
        """
        mappings = {}

        # Reverts the sorted list of numbers.
        inverted_numbers = sorted_numbers[::-1]

        # create min and max indexes for each number.
        for number in sorted_numbers:
            # index first appearance of the number.
            min_index = sorted_numbers.index(number)

            # index of the last appearance of the number.
            max_index = len(sorted_numbers) - inverted_numbers.index(number) - 1

            # min and max index mapped for each number.
            mappings[number] = {"max_index": max_index, "min_index": min_index}
        return mappings

    def build_stats(self):
        """Sorts the list of numbers and returns an object for querying
        statistics about the inputs. The returned object supports
        querying how many numbers in the collection are less than a value, greater
        than a value, or within a range.
        """
        # Create an ordered list using the numbers list.
        # Note: I would normally use list.sort() but I discarded that option
        # since it has a O(n log n) complexity.
        sorted_numbers = self._trimmed_and_sort_numbers()

        # Generates a mappings of the min and max index of each number
        # to later use.
        mappings = self.generate_mappings(sorted_numbers)

        # Return Stats instance.
        return Stats(sorted_numbers, mappings)


if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(stats.less(4))
    print(stats.greater(4))
    print(stats.between(3, 6))
