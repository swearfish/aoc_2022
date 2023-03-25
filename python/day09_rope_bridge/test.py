from unittest import TestCase

from day09_rope_bridge.main import get_part_1_results_from_file, get_part_2_results_from_file


class TestPart1(TestCase):
    def test_part1_example(self):
        self.assertEqual(13, get_part_1_results_from_file('example.in'))

    def test_part1_input(self):
        self.assertEqual(6271, get_part_1_results_from_file('input.in'))


class TestPart2(TestCase):
    def test_part2_example_1(self):
        self.assertEqual(1, get_part_2_results_from_file('example.in'))

    def test_part2_example_2(self):
        self.assertEqual(36, get_part_2_results_from_file('example_2.in'))

    def test_part2_input(self):
        self.assertEqual(2458, get_part_2_results_from_file('input.in'))
