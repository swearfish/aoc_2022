"""
Solutions for Advent of Code 2022 Day 8 puzzle: "Treetop tree house"
https://adventofcode.com/2022/day/8

Copyright (C) 2022. Ákos Nagy
https://www.linkedin.com/in/akosnagy350/
"""


from __future__ import annotations


def get_part_1_results_from_file(file_name: str) -> int:
    forest = read_forest_from_file(file_name)
    return get_visible_trees(forest)


def get_part_2_results_from_file(file_name: str) -> int:
    forest = read_forest_from_file(file_name)
    return get_max_scenic_score(forest)


class Forest:
    def __init__(self, lines: list[str]):
        self._trees = Forest.matrix_from_list(lines)
        self._height = len(self._trees)
        self._width = len(self._trees[0])

    def get_tree_height(self, col: int, row: int):
        return self._trees[row][col]

    def get_scenic_score(self, col: int, row: int):
        h = self.get_tree_height(col, row)
        d = 0
        for i in range(col+1, self.width):
            d += 1
            if h <= self.get_tree_height(i, row):
                break
        result = d
        d = 0
        for i in range(col-1, -1, -1):
            d += 1
            if h <= self.get_tree_height(i, row):
                break
        result *= d
        d = 0
        for i in range(row+1, self.height):
            d += 1
            if h <= self.get_tree_height(col, i):
                break
        result *= d
        d = 0
        for i in range(row-1, -1, -1):
            d += 1
            if h <= self.get_tree_height(col, i):
                break
        result *= d
        return result

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def edge_length(self):
        return 2 * (self.width + self.height) - 4

    @staticmethod
    def matrix_from_list(lines: list[str]) -> list[list[int]]:
        result: list[list[int]] = []
        for line in lines:
            tree_line = []
            for tree in line.strip():
                tree_line.append(int(tree))
            result.append(tree_line)
        return result


def read_forest_from_file(file_name: str) -> Forest:
    with open(file_name) as f:
        lines = f.readlines()
        return Forest(lines)


def get_visible_trees(forest: Forest) -> int:
    maxes: list[list[list[int]]] = [[[10 for _ in range(4)] for _ in range(forest.width)] for _ in range(forest.height)]
    for row in range(0, forest.height):
        max_from_left = 0
        max_from_right = 0
        col2 = forest.width - 1
        for col in range(0, forest.width):
            maxes[row][col][0] = max_from_left
            maxes[row][col2][1] = max_from_right
            max_from_left = max(forest.get_tree_height(col, row), max_from_left)
            max_from_right = max(forest.get_tree_height(col2, row), max_from_right)
            col2 -= 1
    for col in range(0, forest.width):
        max_from_top = 0
        max_from_bottom = 0
        row2 = forest.height - 1
        for row in range(0, forest.height):
            maxes[row][col][2] = max_from_top
            maxes[row2][col][3] = max_from_bottom
            max_from_top = max(forest.get_tree_height(col, row), max_from_top)
            max_from_bottom = max(forest.get_tree_height(col, row2), max_from_bottom)
            row2 -= 1
    visible_count = forest.edge_length
    for row in range(1, forest.height - 1):
        for col in range(1, forest.width - 1):
            tree = forest.get_tree_height(col, row)
            lmax = maxes[row][col]
            is_visible = any(tree > m for m in lmax)
            if is_visible:
                visible_count += 1
    return visible_count


def get_max_scenic_score(forest: Forest):
    max_scenic_score = 0
    for row in range(1, forest.height - 1):
        for col in range(1, forest.width - 1):
            scenic_score = forest.get_scenic_score(col, row)
            max_scenic_score = max(scenic_score, max_scenic_score)
    return max_scenic_score
