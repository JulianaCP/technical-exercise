"""Units test for the DataCapture class."""
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
