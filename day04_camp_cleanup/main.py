"""
Solutions for Advent of Code 2022 Day 4 puzzle: "Camp Cleanup"
https://adventofcode.com/2022/day/4

Copyright (C) 2022. Ákos Nagy
https://www.linkedin.com/in/akosnagy350/
"""


from typing import Optional, Callable


def get_part_1_results_from_file(file_name: str) -> int:
    return get_results_from_file(file_name, contains)


def get_part_2_results_from_file(file_name: str) -> int:
    return get_results_from_file(file_name, overlaps)


def get_results_from_file(file_name: str, fn: Callable[[tuple[int], tuple[int]], bool]) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        return get_results(lines, fn)


def read_ranges(line: str) -> Optional[tuple[tuple[int], tuple[int]]]:
    if '\n' == line:
        return None
    first_elf, second_elf = line.strip().split(',')
    first_elf = tuple(map(lambda x: int(x), first_elf.split('-')))
    second_elf = tuple(map(lambda x: int(x), second_elf.split('-')))
    return first_elf, second_elf


def contains(range1: tuple[int], range2: tuple[int]) -> bool:
    return range1[0] <= range2[0] and range2[1] <= range1[1]


def overlaps(range1: tuple[int], range2: tuple[int]) -> bool:
    return min(range1[1], range2[1]) >= max(range1[0], range2[0])


def get_results(lines: list[str], fn: Callable[[tuple[int], tuple[int]], bool]) -> int:
    result = 0
    for line in lines:
        if '\n' == line:
            break
        first_elf, second_elf = read_ranges(line)
        if fn(first_elf, second_elf) or fn(second_elf, first_elf):
            result += 1
    return result
