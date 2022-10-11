"""Units test for the DataCapture and
the Stats class.
"""
from unittest import TestCase

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

    def test_add_method(self):
        """Checks that the numbers were added successfully."""
        self.assertEqual(sum(self.data_capture.numbers_existence), 6)

    def test_trimmed_sort_numbers(self):
        """Checks if the sort method is ordering the numbers correctly."""
        sorted_numbers = self.data_capture._trimmed_and_sort_numbers()
        self.assertTrue(sorted_numbers, [1, 2, 3, 4, 5, 6])

    def test_mappings(self):
        """Checks if the sort method is ordering the numbers correctly."""
        sorted_numbers = self.data_capture._trimmed_and_sort_numbers()
        self.assertTrue(sorted_numbers, [1, 2, 3, 4, 5, 6])

    def test_build_stats_method(self):
        """Checks that the build stats method is actually returning an object."""
        stats = self.data_capture.build_stats()
        self.assertIsInstance(stats, Stats)


class TestStatsMethods(TestCase):
    """Tests the methods of Stats object."""
    def setUp(self) -> None:
        """Creates the dataCapture instance, adds 6 numbers to the list
        and creates a stats object with the dataCapture status.
        """
        self.data_capture = DataCapture()
        self.data_capture.add(3)
        self.data_capture.add(9)
        self.data_capture.add(3)
        self.data_capture.add(4)
        self.data_capture.add(6)
        self.stats = self.data_capture.build_stats()

    def test_stats_less_method(self):
        """Checks that the stats lower method is finding correctly
        the numbers lower than X, if the sent number is 4.
        """
        number = 4
        numbers_lower_than_4 = self.stats.less(number)
        self.assertEqual(numbers_lower_than_4, [3, 3])

    def test_stats_greater_method(self):
        """Checks that the stats greater method is finding correctly
        the numbers greater than X, if the sent number is 4.
        """
        number = 4
        numbers_greater_than_4 = self.stats.greater(number)
        self.assertEqual(numbers_greater_than_4, [6, 9])

    def test_stats_between_method(self):
        """Checks that the stats between method is finding correctly
        the numbers between X and Y, if the sent numbers are 3 and 6.
        """
        min_number = 3
        max_number = 6
        numbers_between_3_and_6 = self.stats.between(min_number, max_number)
        self.assertEqual(numbers_between_3_and_6, [3, 3, 4, 6])
