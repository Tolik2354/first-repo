import unittest
from python import calculate_overdue_days, calculate_fine


class TestLibraryFunctions(unittest.TestCase):

    def test_overdue_days(self):
        self.assertEqual(calculate_overdue_days(10, 7), 3)
        self.assertEqual(calculate_overdue_days(5, 7), 0)
        self.assertEqual(calculate_overdue_days(7, 7), 0)

    def test_fine(self):
        self.assertEqual(calculate_fine(3, 2.0), 6.0)
        self.assertEqual(calculate_fine(0, 5.0), 0.0)
        self.assertEqual(calculate_fine(5, 1.5), 7.5)


if __name__ == "__main__":
    unittest.main()