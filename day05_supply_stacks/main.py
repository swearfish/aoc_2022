from typing import Optional, Callable


def get_part_1_results_from_file(file_name: str) -> str:
    return get_results_from_file(file_name, lambda lines: Stacks.execute(lines, model_9001=False))


def get_part_2_results_from_file(file_name: str) -> str:
    return get_results_from_file(file_name, lambda lines: Stacks.execute(lines, model_9001=True))


def get_results_from_file(file_name: str, fn: Callable[[list[str]], str]) -> str:
    with open(file_name) as f:
        lines = f.readlines()
        return fn(lines)


class Move:
    def __init__(self, line: str):
        parts = line.strip().split(' ')
        self.count = int(parts[1])
        self.src = parts[3]
        self.dst = parts[5]


class Stacks:
    def __init__(self, lines: list[str], model_9001: bool = False):
        sep = lines.index('\n')
        assert sep != ValueError
        self.moves = Stacks.read_moves(lines[sep+1: ])
        self.indices = Stacks.find_indices(lines[sep-1])
        self.columns = Stacks.load_columns(lines[0: sep-1], self.indices)
        self.reverse_moves = not model_9001

    def apply(self, move: Move):
        moved: list = self.columns[move.src][0: move.count]
        self.columns[move.src] = self.columns[move.src][move.count: ]
        if self.reverse_moves:
            moved.reverse()
        self.columns[move.dst] = [*moved, *self.columns[move.dst]]

    def apply_all(self, moves: list[Move]):
        for move in moves:
            self.apply(move)

    def apply_all_moves(self):
        return self.apply_all(self.moves)

    def get_top(self) -> str:
        result = ""
        for index in self.columns:
            column = self.columns[index]
            if 0 < len(self.columns):
                top = column[0]
                result += top
        return result

    @staticmethod
    def read_moves(lines: list[str]) -> list[Move]:
        result = []
        for line in lines:
            result.append(Move(line))
        return result

    @staticmethod
    def find_indices(line: str) -> dict[str, int]:
        result = {}
        index = 0
        while index < len(line):
            if line[index] != ' ':
                column = ""
                start = index
                while line[index] not in (' ', '\n'):
                    column += line[index]
                    index += 1
                result[column] = start
            index += 1
        return result

    @staticmethod
    def load_columns(lines: list[str], indices: dict[str, int]) -> dict[str, list[str]]:
        result = {}
        for index in indices:
            result[index] = []
        for line in lines:
            for index in indices:
                pos = indices[index]
                if len(line) <= pos:
                    break
                item = line[pos]
                if item != ' ':
                    result[index].append(item)
        return result

    @staticmethod
    def execute(lines: list[str], model_9001: bool = False) -> str:
        stacks = Stacks(lines, model_9001=model_9001)
        stacks.apply_all_moves()
        return stacks.get_top()