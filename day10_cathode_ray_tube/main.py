"""
Solutions for Advent of Code 2022 Day 10 puzzle: "Cathode-ray tube"
https://adventofcode.com/2022/day/10

Copyright (C) 2022. Ákos Nagy
https://www.linkedin.com/in/akosnagy350/
"""


from __future__ import annotations


def get_part_1_results_from_file(file_name: str) -> int:
    commands = read_file(file_name)
    return get_signal_strength(commands)


def get_part_2_results_from_file(file_name: str) -> int:
    commands = read_file(file_name)
    return get_signal_strength(commands)


CYCLE_COUNT = {
    'noop': 1,
    'addx': 2
}


class Inst:
    def __init__(self, line: str):
        parts = line.strip().split(' ')
        self.op_code = parts[0]
        if 1 < len(parts):
            self.operand = int(parts[1])
        else:
            self.operand = None
        assert self.op_code in CYCLE_COUNT
        self.cycles = CYCLE_COUNT[self.op_code]

    def __repr__(self):
        if self.operand is not None:
            return f'{self.op_code} {self.operand}'
        return f'{self.op_code}'


class VM:
    def __init__(self):
        self.x = 1
        self.cycles = 1
        self.prev_sum_cycle = -20
        self.total_signal_strength = 0
        self.ops = {
            'addx': self.addx,
            'noop': self.noop
        }

    def execute_inst(self, inst: Inst):
        next_cycles = self.cycles + inst.cycles
        self.update_signal_strength(next_cycles - 1)
        assert inst.op_code in self.ops
        old_x = self.x
        old_cycles = self.cycles
        fn = self.ops[inst.op_code]
        fn(inst.operand)
        self.cycles += inst.cycles
        self.update_signal_strength(self.cycles)
        # print(f'[{inst}]: [x:{old_x}, c:{old_cycles}] --> [x:{self.x}, c:{self.cycles}]')

    def execute_code(self, code: list[Inst]):
        for inst in code:
            self.execute_inst(inst)

    def update_signal_strength(self, cycles: int):
        if cycles == self.prev_sum_cycle:
            return
        next = self.prev_sum_cycle + 40
        if next <= cycles:
            signal_strength = next * self.x
            # print(f'{self.__repr__()} :: {next} x {self.x} = {signal_strength}')
            self.total_signal_strength += signal_strength
            self.prev_sum_cycle = cycles

    def noop(self, _op):
        pass

    def addx(self, operand: int):
        self.x += operand

    def __repr__(self):
        return f'x:{self.x} c:{self.cycles} s:{self.total_signal_strength}'


def read_file(file_name: str) -> list[Inst]:
    with open(file_name) as f:
        lines = f.readlines()
        code = []
        for line in lines:
            code.append(Inst(line))
        return code


def get_signal_strength(code: list[Inst]) -> int:
    vm = VM()
    vm.execute_code(code)
    return vm.total_signal_strength
