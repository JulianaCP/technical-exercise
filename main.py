"""
Data Capture class and stats object.

This class provides functions for calculating statistics of data, including
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
[3, 3]


Numbers between X and Y:

>> capture = DataCapture()
>> capture.add(3)
>> capture.add(9)
>> capture.add(3)
>> capture.add(4)
>> capture.add(6)
>> stats = capture.build_stats()
>> stats.between(3, 6)
[3, 3, 4, 6]


Numbers greater than X:

>> capture = DataCapture()
>> capture.add(3)
>> capture.add(9)
>> capture.add(3)
>> capture.add(4)
>> capture.add(6)
>> stats = capture.build_stats()
>> stats.between(3, 6)
[6, 9]


Decorators
----------

A single decorator is defined: check_arguments is a decorator that
checks that all of the receives arguments for each of the stats
methods are integers.
"""
from queue import PriorityQueue


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


class DataCapture:
    """The DataCapture object accepts numbers and returns an object for querying
    statistics about the inputs. Specifically, the returned object supports
    querying how many numbers in the collection are less than a value, greater
    than a value, or within a range.
    """
    def __init__(self):
        # O(1) complexity.
        self._numbers = []

    @property
    def numbers(self):
        """Returns the private attribute numbers, that contains
        the list with numbers.
        """
        return self._numbers

    def add(self, number):
        """Adds a number to the numbers list (available numbers to
        manipulate and generate the stats).
        """
        # O(1) complexity.
        self._numbers.append(number)

    @check_arguments
    def less(self, number, number_to_check=None):
        """Checks if the sent number is lower than X (being X
        the number to check that will represent an element
        in the list). In case no number to check was
        sent, the method will return false by default.

        :param int number: Stats number.
        :param int, None number_to_check: Number to check. Method with
        check if the 'number' is lower than this number.
        """
        # O(1) complexity.
        return number < number_to_check if number_to_check else False

    @check_arguments
    def between(self, number, min_number=None, max_number=None):
        """Checks if the sent number is between X and Y (being X
        the minimum number to check and Y the maximum number to
        check. Both values represent an interval and this method
        will check if the sent number is between this interval.
        In case no min or max number were, the method will
        return false by default.

        :param int number: Stats number.
        :param int, None min_number: Minimum number to check. Method with
        check if the 'number' is greater than this number.
        :param int, None max_number: Maximum number to check. Method with
        check if the 'number' is lower than this number.
        """
        # O(1) complexity.
        return min_number <= number <= max_number if min_number and max_number else False

    @check_arguments
    def greater(self, number, number_to_check=None):
        """Checks if the sent number is greater than X (being X
        the number to check that will represent an element
        in the list). In case no number to check was
        sent, the method will return false by default.

        :param int number: Stats number.
        :param int, None number_to_check: Number to check. Method with
        check if the 'number' is greater than this number.
        """
        # O(1) complexity.
        return number > number_to_check if number_to_check else False

    def _searcher(self, numbers, validator, *args, selections=None):
        """This is a recursive function to find all the numbers inside a list that
        passed a validation (validation could be 'numbers lower than X',
        'numbers between than X and Y' and 'numbers greater than X'). At the
        end of the execution it will return the list  of all of the numbers
        that passed the validation.

        :param list numbers: Number of the list.
        :param function validator: Validation could be 'numbers lower than X',
        'numbers between than X and Y' and 'numbers greater than X'.
        :param tuple, int args: Inputs of the validation function.
        :param list, None selections: Number that passed the restriction.
        """
        # O(n) complexity.
        # We can assume all values will be less than 1,000 so the recursion
        # will not failed.
        if not selections:
            selections = []

        # if there isn't more numbers to process, stop recursion and return
        # the extracted numbers.
        if not numbers:
            return selections

        # add number and keep analyzing
        if validator(numbers[0], *args):
            selections.append(numbers[0])

        # keep processing the list of numbers.
        return self._searcher(numbers[1:], validator, *args, selections=selections)

    def _sort_numbers(self):
        """Uses the heapq module in Python to create a priority queue.
        This implementation has O(log n) time for insertion and extraction.
        The PriorityQueue uses the same heapq implementation internally and
        thus has the same time complexity (PriorityQueue is the classic OOP style
        of implementing and using Priority Queues).

        The priority queue is an advanced type of the queue data structure.
        Instead of dequeuing the oldest element, a priority queue sorts
        and dequeues elements based on their priorities. Since the
        queue.PriorityQueue class needs to maintain the order of
        its elements, a sorting mechanism is required every time a new
        element is enqueued. Python solves this by using a binary heap
        to implement the priority queue. The Python priority
        queue is built on the heapq module, which is basically a
        binary heap with O(n) complexity.
        """
        # O(1) complexity.
        # we initialise the PriorityQueue class to operate upon a list.
        sorted_queue_numbers = PriorityQueue()
        for number in self._numbers:
            # Insertion	O(log n) complexity.
            # Puts an number into the queue (It will be adding the numbers
            # in ordered).
            sorted_queue_numbers.put(number)

        # O(n) complexity.
        # generates a ordered list with the sorted queue.
        sorted_numbers = []
        while not sorted_queue_numbers.empty():
            # Deletion O(log n) complexity.
            # The get command dequeues the highest priority elements from the queue.
            # here we are going to be adding one by one all the values of
            # the ordered queue to a list, basically we are moving from a
            # ordered priorityQueue to a ordered list (will be easier
            # to use lists to handle the 'less', 'greater' and 'between'
            # methods with lists instead of a a queue).
            sorted_numbers.append(sorted_queue_numbers.get())

        return sorted_numbers

    def build_stats(self):
        """Sorts the list of numbers and returns an object for querying
        statistics about the inputs. The returned object supports
        querying how many numbers in the collection are less than a value, greater
        than a value, or within a range.
        """
        # O(n) complexity
        # create an ordered list using the numbers list.
        # Note: I would normally use list.sort() but I discarded that option
        # since it has a O(n log n) complexity. So, in regards of the
        # requirement I implemented a priorityQueue, more details in the
        # sort numbers method.
        sorted_numbers = self._sort_numbers()

        # O(n) complexity
        # Dynamic Stats class to handle calls on less, greater and between methods.
        return type("Stats", (object,), {
            "_sorted_numbers": sorted_numbers,
            "less": lambda cls, n: self._searcher(cls._sorted_numbers, self.less, n),
            "greater": lambda cls, n: self._searcher(cls._sorted_numbers, self.greater, n),
            "between": lambda cls, min_n, max_n: self._searcher(cls._sorted_numbers, self.between, min_n, max_n)
        })()


if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(f"'less(4)' = {stats.less(4)}")
    print(f"'greater(4)' = {stats.greater(4)}")
    print(f"'between(3, 6)' = {stats.between(3, 6)}")
