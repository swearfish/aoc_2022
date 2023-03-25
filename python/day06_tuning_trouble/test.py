from unittest import TestCase

from day06_tuning_trouble.main import get_chars_before_message, get_chars_before_message_in_file, HEAD_LEN_PART_1, \
    HEAD_LEN_PART_2


class TestPart1(TestCase):
    def test_example_1(self):
        self.assertEqual(7, get_chars_before_message('mjqjpqmgbljsphdztnvjfqwrcgsmlb', HEAD_LEN_PART_1))

    def test_example_2(self):
        self.assertEqual(5, get_chars_before_message('bvwbjplbgvbhsrlpgdmjqwftvncz', HEAD_LEN_PART_1))

    def test_example_3(self):
        self.assertEqual(6, get_chars_before_message('nppdvjthqldpwncqszvftbrmjlhg', HEAD_LEN_PART_1))

    def test_example_4(self):
        self.assertEqual(10, get_chars_before_message('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', HEAD_LEN_PART_1))

    def test_example_5(self):
        self.assertEqual(11, get_chars_before_message('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', HEAD_LEN_PART_1))

    def test_input(self):
        self.assertEqual(1034, get_chars_before_message_in_file('input.in', HEAD_LEN_PART_1))


class TestPart2(TestCase):
    def test_example_1(self):
        self.assertEqual(19, get_chars_before_message('mjqjpqmgbljsphdztnvjfqwrcgsmlb', HEAD_LEN_PART_2))

    def test_example_2(self):
        self.assertEqual(23, get_chars_before_message('bvwbjplbgvbhsrlpgdmjqwftvncz', HEAD_LEN_PART_2))

    def test_example_3(self):
        self.assertEqual(23, get_chars_before_message('nppdvjthqldpwncqszvftbrmjlhg', HEAD_LEN_PART_2))

    def test_example_4(self):
        self.assertEqual(29, get_chars_before_message('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', HEAD_LEN_PART_2))

    def test_example_5(self):
        self.assertEqual(26, get_chars_before_message('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', HEAD_LEN_PART_2))

    def test_input(self):
        self.assertEqual(2472, get_chars_before_message_in_file('input.in', HEAD_LEN_PART_2))

