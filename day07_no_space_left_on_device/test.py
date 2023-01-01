from unittest import TestCase

from day07_no_space_left_on_device.main import get_part_1_results_from_file, get_part_2_results_from_file


class TestPart1(TestCase):
    def test_part1_example(self):
        self.assertEqual(95437, get_part_1_results_from_file('example.in'))

    def test_part1_input(self):
        self.assertEqual(1770595, get_part_1_results_from_file('input.in'))


class TestPart2(TestCase):
    def test_part2_example(self):
        self.assertEqual(24933642, get_part_2_results_from_file('example.in'))

    def test_part2_input(self):
        self.assertEqual(2195372, get_part_2_results_from_file('input.in'))
