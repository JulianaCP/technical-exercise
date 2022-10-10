from unittest import TestCase

from main import DataCapture


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
        self.assertEqual(len(self.data_capture.numbers), 6)

    def test_less_method(self):
        """Checks that the less method validation method is working properly.
        The less method validation checks which numbers in the list should
        be consider lower than X, if X is consider 2.
        """
        # selected K = 2
        self.assertTrue(self.data_capture.less(1, 2))  # 1 < 2 = True
        self.assertFalse(self.data_capture.less(2, 2))  # 2 < 2 = False
        self.assertFalse(self.data_capture.less(3, 2))  # 3 < 2 = False
        self.assertFalse(self.data_capture.less(4, 2))  # 4 < 2 = False
        self.assertFalse(self.data_capture.less(5, 2))  # 5 < 2 = False
        self.assertFalse(self.data_capture.less(6, 2))  # 6 < 2 = False

    def test_greater_method(self):
        """Checks that the greater method validation method is working properly.
        The greater method validation checks which numbers in the list should
        be consider greater than X, if X is consider 2.
        """
        # selected K = 2
        self.assertFalse(self.data_capture.greater(1, 2))  # 1 > 2 = False
        self.assertFalse(self.data_capture.greater(2, 2))  # 2 > 2 = False
        self.assertTrue(self.data_capture.greater(3, 2))  # 3 > 2 = True
        self.assertTrue(self.data_capture.greater(4, 2))  # 4 > 2 = True
        self.assertTrue(self.data_capture.greater(5, 2))  # 5 > 2 = True
        self.assertTrue(self.data_capture.greater(6, 2))  # 6 > 2 = True

    def test_between_method(self):
        """Checks that the between method validation method is working properly.
        The between method validation checks which numbers in the list are between
        X and Y, if X is consider 2 and Y equals to 4.
        """
        # selected min = 2 and max = 4
        self.assertFalse(self.data_capture.between(1, 2, 4))  # 2 <= 1 <= 4 = False
        self.assertTrue(self.data_capture.between(2, 2, 4))  # 2 <= 2 <= 4 = True
        self.assertTrue(self.data_capture.between(3, 2, 4))  # 2 <= 3 <= 4 = True
        self.assertTrue(self.data_capture.between(4, 2, 4))  # 2 <= 4 <= 4 = True
        self.assertFalse(self.data_capture.between(5, 2, 4))  # 2 <= 5 <= 4 = False
        self.assertFalse(self.data_capture.between(6, 2, 4))  # 2 <= 6 <= 4 = False

    def test_sort_numbers(self):
        """Checks if the sort method is ordering the numbers correctly."""
        sorted_numbers = self.data_capture._sort_numbers()
        self.assertTrue(sorted_numbers, [1, 2, 3, 4, 5, 6])

    def test_less_searcher(self):
        """Checks that the recursive function searcher is finding correctly
        the numbers lower than X, if the validation method is less and the
        X value is 4.
        """
        sorted_numbers = self.data_capture._sort_numbers()
        number = 4
        numbers_lower_than_4 = self.data_capture._searcher(sorted_numbers, self.data_capture.less, number)
        self.assertEqual(numbers_lower_than_4, [1, 2, 3])

    def test_greater_searcher(self):
        """Checks that the recursive function searcher is finding correctly
        the numbers greater than X, if the validation method is between and the
        X value is 4.
        """
        sorted_numbers = self.data_capture._sort_numbers()
        number = 4
        numbers_greater_than_4 = self.data_capture._searcher(sorted_numbers, self.data_capture.greater, number)
        self.assertEqual(numbers_greater_than_4, [5, 6])

    def test_between_searcher(self):
        """Checks that the recursive function searcher is finding correctly
        the numbers between X and Y, if the validation method is greater and the
        X value is 2 and Y equals to 5.
        """
        sorted_numbers = self.data_capture._sort_numbers()
        min_number = 2
        max_number = 5
        numbers_between_2_and_5 = self.data_capture._searcher(sorted_numbers, self.data_capture.between,
                                                              min_number, max_number)
        self.assertEqual(numbers_between_2_and_5, [2, 3, 4, 5])

    def test_build_stats_method(self):
        """Checks that the build stats method is actually returning an object."""
        stats = self.data_capture.build_stats()
        self.assertIsInstance(stats, object)


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
