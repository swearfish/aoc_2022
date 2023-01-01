from unittest import TestCase

from day04_camp_cleanup.main import get_part_1_results_from_file, get_part_2_results_from_file


class Test(TestCase):
    def test_part1_example(self):
        self.assertEqual(2, get_part_1_results_from_file('example.in'))

    def test_part1_input(self):
        self.assertEqual(526, get_part_1_results_from_file('input.in'))

    def test_part2_example(self):
        self.assertEqual(4, get_part_2_results_from_file('example.in'))

    def test_part2_input(self):
        self.assertEqual(886, get_part_2_results_from_file('input.in'))
