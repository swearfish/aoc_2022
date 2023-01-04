from unittest import TestCase

from day10_cathode_ray_tube.main import get_part_1_results_from_file, get_part_2_results_from_file, \
    read_display_from_file


class TestPart1(TestCase):

    def test_simple(self):
        self.assertEqual(0, get_part_1_results_from_file('simple.in'))

    def test_part1_example(self):
        self.assertEqual(13140, get_part_1_results_from_file('example.in'))

    def test_part1_input(self):
        self.assertEqual(14040, get_part_1_results_from_file('input.in'))


class TestPart2(TestCase):
    def test_part2_example(self):
        actual_display = get_part_2_results_from_file('example.in')
        expected_display = read_display_from_file('example.out')
        self.assertEqual(expected_display, actual_display)

    def test_part2_input(self):
        actual_display = get_part_2_results_from_file('input.in')
        expected_display = read_display_from_file('input.out')
        self.assertEqual(expected_display, actual_display)
