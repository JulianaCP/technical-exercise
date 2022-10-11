"""Units test for the DataCapture and
the Stats class.
"""
from unittest import TestCase

import pytest

from data_capture.data_capture import DataCapture
from data_capture.stats import Stats


class TestDataCaptureMethods(TestCase):
    """Tests the methods of the DataCapture class."""
    def setUp(self) -> None:
        """Creates the dataCapture instance and adds 6 numbers to the list."""
        self.data_capture = DataCapture()
        self.data_capture.add(4)
        self.data_capture.add(5)
        self.data_capture.add(2)
        self.data_capture.add(3)
        self.data_capture.add(6)
        self.data_capture.add(1)

    def test_add_method(self) -> None:
        """Checks that the numbers were added successfully."""
        self.assertEqual(sum(self.data_capture.numbers_existence), 6)

    def test_trimmed_sort_numbers(self) -> None:
        """Checks if the sort method is ordering the numbers correctly."""
        sorted_numbers = self.data_capture._trimmed_and_sort_numbers()
        self.assertTrue(sorted_numbers, [1, 2, 3, 4, 5, 6])

    def test_mappings(self) -> None:
        """Checks if the sort method is ordering the numbers correctly."""
        sorted_numbers = self.data_capture._trimmed_and_sort_numbers()
        mappings = self.data_capture.generate_mappings(sorted_numbers)
        mapping = {1: {'min_index': 0, 'max_index': 0},
                   2: {'min_index': 1, 'max_index': 1},
                   3: {'min_index': 2, 'max_index': 2},
                   4: {'min_index': 3, 'max_index': 3},
                   5: {'min_index': 4, 'max_index': 4},
                   6: {'min_index': 5, 'max_index': 5}}
        self.assertEqual(mappings, mapping)

    def test_build_stats_method(self) -> None:
        """Checks that the build stats method is actually returning an object."""
        stats = self.data_capture.build_stats()
        self.assertIsInstance(stats, Stats)

    def test_invalid_argument_type(self):
        """Raise value error if the argument
        type sent to the add method is not
        integer.
        """
        with pytest.raises(ValueError):
            self.data_capture.add(3.1)

    def test_add_method_with_limit_range(self):
        """Check if the  range limits can be process and
        add in the list.
        """
        self.assertEqual(sum(self.data_capture.numbers_existence), 6)
        self.data_capture.add(0)
        self.data_capture.add(1000)
        self.assertEqual(sum(self.data_capture.numbers_existence), 8)

    def test_add_method_with_invalid_range(self):
        """Raise value error if the
        number sent to the add method is not
        between the range (0-1000 -> inclusive).
        """
        with pytest.raises(ValueError):
            self.data_capture.add(1001)

        with pytest.raises(ValueError):
            self.data_capture.add(-1)


class TestStatsMethods(TestCase):
    """Tests the methods of Stats object."""
    def setUp(self) -> None:
        """Creates the dataCapture instance, adds 6 numbers to the list
        and creates a stats object with the dataCapture status.
        """
        self.data_capture = DataCapture()
        self.data_capture.add(1)
        self.data_capture.add(3)
        self.data_capture.add(5)
        self.data_capture.add(7)
        self.data_capture.add(8)
        self.data_capture.add(9)
        self.data_capture.add(10)
        self.data_capture.add(6)
        self.data_capture.add(4)
        self.data_capture.add(2)
        self.stats = self.data_capture.build_stats()

    def test_stats_less_method(self) -> None:
        """Checks that the stats lower method is finding correctly
        the numbers lower than X.
        """
        self.assertEqual(self.stats.less(-1), 0)
        self.assertEqual(self.stats.less(0), 0)
        self.assertEqual(self.stats.less(1), 0)
        self.assertEqual(self.stats.less(2), 1)
        self.assertEqual(self.stats.less(3), 2)
        self.assertEqual(self.stats.less(4), 3)
        self.assertEqual(self.stats.less(5), 4)
        self.assertEqual(self.stats.less(6), 5)
        self.assertEqual(self.stats.less(7), 6)
        self.assertEqual(self.stats.less(8), 7)
        self.assertEqual(self.stats.less(9), 8)
        self.assertEqual(self.stats.less(10), 9)
        self.assertEqual(self.stats.less(11), 10)
        self.assertEqual(self.stats.less(12), 10)
        self.assertEqual(self.stats.less(200), 10)

    def test_stats_greater_method(self) -> None:
        """Checks that the stats greater method is finding correctly
        the numbers greater than X.
        """
        self.assertEqual(self.stats.greater(-1), 10)
        self.assertEqual(self.stats.greater(0), 10)
        self.assertEqual(self.stats.greater(1), 9)
        self.assertEqual(self.stats.greater(2), 8)
        self.assertEqual(self.stats.greater(3), 7)
        self.assertEqual(self.stats.greater(4), 6)
        self.assertEqual(self.stats.greater(5), 5)
        self.assertEqual(self.stats.greater(6), 4)
        self.assertEqual(self.stats.greater(7), 3)
        self.assertEqual(self.stats.greater(8), 2)
        self.assertEqual(self.stats.greater(9), 1)
        self.assertEqual(self.stats.greater(10), 0)
        self.assertEqual(self.stats.greater(11), 0)
        self.assertEqual(self.stats.greater(12), 0)
        self.assertEqual(self.stats.greater(200), 0)

    def test_stats_between_method(self) -> None:
        """Checks that the stats between method is finding correctly
        the numbers between X and Y, if the sent numbers are 3 and 6.
        """
        self.assertEqual(self.stats.between(0, 1), 1)
        self.assertEqual(self.stats.between(0, 10), 10)
        self.assertEqual(self.stats.between(-1, 5), 5)
        self.assertEqual(self.stats.between(2, 6), 5)
        self.assertEqual(self.stats.between(3, 8), 6)
        self.assertEqual(self.stats.between(4, 200), 7)
        self.assertEqual(self.stats.between(5, 40), 6)
        self.assertEqual(self.stats.between(6, 8), 3)
        self.assertEqual(self.stats.between(6, 6), 1)
        self.assertEqual(self.stats.between(8, 10), 3)
        self.assertEqual(self.stats.between(9, 10), 2)
        self.assertEqual(self.stats.between(10, 15), 1)
        self.assertEqual(self.stats.between(-1, 8), 8)
        self.assertEqual(self.stats.between(12, 18), 0)
        self.assertEqual(self.stats.between(200, 500), 0)

    def test_greater_method_with_invalid_argument_type(self):
        """Raise value error if the argument
        type sent to the greater method is not
        integer.
        """
        with pytest.raises(ValueError):
            self.stats.greater(3.1)

    def test_less_method_with_invalid_argument_type(self):
        """Raise value error if the argument
        type sent to the less method is not
        integer.
        """
        with pytest.raises(ValueError):
            self.stats.less(3.1)

    def test_between_method_with_invalid_argument_type(self):
        """Raise value error if the arguments
        send to the between method are not
        integer.
        """
        with pytest.raises(ValueError):
            self.stats.between(0, 3.1)

        with pytest.raises(ValueError):
            self.stats.between(3.1, 5)

        with pytest.raises(ValueError):
            self.stats.between(3.1, 5.5)

    def test_between_method_with_higher_number_in_the_first_argument(self):
        """Checks that the between method can handle
        the range when the first provided argument in higher
        than the second argument.
        """
        self.assertEqual(self.stats.between(500, 0), 10)
        self.assertEqual(self.stats.between(5, 2), 4)

