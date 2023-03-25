from unittest import TestCase

from day03_rucksack_reorganization.main import get_error_sum_from_file, get_badge_sum_from_file


class Test(TestCase):
    def test_get_error_prio_sum_example(self):
        self.assertEqual(157, get_error_sum_from_file('example.in'))

    def test_get_error_prio_sum_input(self):
        self.assertEqual(7795, get_error_sum_from_file('input.in'))

    def test_get_badge_prio_sum_example(self):
        self.assertEqual(70, get_badge_sum_from_file('example.in'))

    def test_get_badge_prio_sum_input(self):
        self.assertEqual(2703, get_badge_sum_from_file('input.in'))

