from unittest import TestCase

from day08_treetop_tree_house.main import get_part_1_results_from_file, get_part_2_results_from_file


class TestPart1(TestCase):
    def test_part1_example(self):
        self.assertEqual(21, get_part_1_results_from_file('example.in'))

    def test_part1_input(self):
        self.assertEqual(1717, get_part_1_results_from_file('input.in'))


class TestPart2(TestCase):
    def test_part2_example(self):
        self.assertEqual(8, get_part_2_results_from_file('example.in'))

    def test_part2_input(self):
        self.assertEqual(321975, get_part_2_results_from_file('input.in'))
