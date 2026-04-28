import unittest
from prog import calculate_overdue_days, calculate_fine


class TestLibraryFunctions(unittest.TestCase):

    def test_overdue_days(self):
        for return_day, deadline, expected in [(10, 7, 4), (5, 7, 0), (7, 7, 1)]:
            with self.subTest("Check overdue", return_day=return_day):
                self.assertEqual(calculate_overdue_days(return_day, deadline), expected)

    def test_fine(self):
        self.assertEqual(calculate_fine(3, 2.0), 6.0)
        self.assertEqual(calculate_fine(0, 5.0), 0.0)
        self.assertEqual(calculate_fine(5, 1.5), 7.5)


if __name__ == "__main__":
    unittest.main()