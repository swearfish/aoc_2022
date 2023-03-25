from unittest import TestCase

from day01_calorie_counting.main import find_max_calories, find_top_3_calories


class TestCalorieCounting(TestCase):
    def test_example_max(self):
        self.assertEqual(24000, find_max_calories('example.in'))

    def test_example_top_3(self):
        self.assertEqual(45000, find_top_3_calories('example.in'))

    def test_input_max(self):
        self.assertEqual(70374, find_max_calories('input.in'))

    def test_input_top_3(self):
        self.assertEqual(204610, find_top_3_calories('input.in'))