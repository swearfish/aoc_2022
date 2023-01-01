from unittest import TestCase

from day02_rock_paper_scissors.rock_paper_scissors import get_score_from_file, SCORE_TABLE, SCORE_TABLE_PART_TWO


class Test(TestCase):
    def test_example_score(self):
        self.assertEqual(15, get_score_from_file('example.in', SCORE_TABLE))

    def test_input_score(self):
        self.assertEqual(9651, get_score_from_file('input.in', SCORE_TABLE))

    def test_example_score_part_two(self):
        self.assertEqual(12, get_score_from_file('example.in', SCORE_TABLE_PART_TWO))

    def test_input_score_part_two(self):
        self.assertEqual(10560, get_score_from_file('input.in', SCORE_TABLE_PART_TWO))
