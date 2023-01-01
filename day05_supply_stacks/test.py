from unittest import TestCase

from day05_supply_stacks.main import get_part_1_results_from_file, get_part_2_results_from_file


class Test(TestCase):
    def test_part1_example(self):
        self.assertEqual("CMZ", get_part_1_results_from_file('example.in'))

    def test_part1_input(self):
        self.assertEqual("SHQWSRBDL", get_part_1_results_from_file('input.in'))

    def test_part2_example(self):
        self.assertEqual("MCD", get_part_2_results_from_file('example.in'))

    def test_part2_input(self):
        self.assertEqual("CDTQZHBRS", get_part_2_results_from_file('input.in'))
