"""
Solutions for Advent of Code 2022 Day 10 puzzle: "Cathode-ray tube"
https://adventofcode.com/2022/day/10

Copyright (C) 2022. Ákos Nagy
https://www.linkedin.com/in/akosnagy350/
"""


from __future__ import annotations


def get_part_1_results_from_file(file_name: str) -> int:
    commands = read_instructions_from_file(file_name)
    return get_signal_strength(commands)


def get_part_2_results_from_file(file_name: str) -> str:
    commands = read_instructions_from_file(file_name)
    return get_display(commands)


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

    STAGE_CYCLE_TIME = 0
    STAGE_PRE_EXEC = 1
    STAGE_POST_EXEC = 2

    def __init__(self):
        self.x = 1
        self.cycle = 1
        self.ops = {
            'addx': self.addx,
            'noop': self.noop
        }

    def update_cycle(self, inst: Inst, stage: int):
        pass

    def execute_inst(self, inst: Inst):
        for current_cycle in range(inst.cycles-1):
            self.cycle += 1
            self.update_cycle(inst, VM.STAGE_CYCLE_TIME)
        self.cycle += 1
        self.update_cycle(inst, VM.STAGE_PRE_EXEC)
        assert inst.op_code in self.ops, f'Unknown opcode: {inst.op_code}'
        fn = self.ops[inst.op_code]
        fn(inst.operand)
        self.update_cycle(inst, VM.STAGE_POST_EXEC)

    def execute_code(self, code: list[Inst]):
        for inst in code:
            self.execute_inst(inst)

    def noop(self, _op):
        pass

    def addx(self, operand: int):
        self.x += operand


class SignalStrengthVM(VM):

    def __init__(self):
        super().__init__()
        self.total_signal_strength = 0

    def update_cycle(self, inst: Inst, stage: int):
        if stage != VM.STAGE_PRE_EXEC and ((self.cycle + 20) % 40) == 0:
            signal_strength = self.cycle * self.x
            self.total_signal_strength += signal_strength

    def __repr__(self):
        return f'x:{self.x} c:{self.cycle} s:{self.total_signal_strength}'


class TubeVM(VM):

    SCREEN_WIDTH = 40
    SCREEN_HEIGHT = 6

    def __init__(self):
        super().__init__()
        self.framebuffer: list[list[str]] = \
            [["." for _ in range(TubeVM.SCREEN_WIDTH)] for _ in range(TubeVM.SCREEN_HEIGHT)]
        self.ray_x = 0
        self.ray_y = 0

    def update_cycle(self, inst: Inst, stage: int):
        if stage != VM.STAGE_POST_EXEC:
            self._draw()
            self._adjust_ray()

    def _adjust_ray(self):
        self.ray_x += 1
        if self.ray_x == TubeVM.SCREEN_WIDTH:
            self.ray_x = 0
            self.ray_y += 1
            if self.ray_y == TubeVM.SCREEN_HEIGHT:
                self.ray_y = 0

    def _draw(self):
        pixel = "#" if self.x - 1 <= self.ray_x <= self.x + 1 else "."
        self.framebuffer[self.ray_y][self.ray_x] = pixel

    def __str__(self):
        lines = ["".join(line) for line in self.framebuffer]
        display = "\n".join(lines)
        return display

    def __repr__(self):
        return f'x:{self.x} c:{self.cycle} r:{self.ray_x, self.ray_x}\n{self.__str__()}'


def read_instructions_from_file(file_name: str) -> list[Inst]:
    lines = read_file(file_name)
    code = []
    for line in lines:
        code.append(Inst(line))
    return code


def read_display_from_file(file_name: str) -> str:
    lines = read_file(file_name)
    return "".join(lines).strip()


def read_file(file_name: str) -> list[str]:
    with open(file_name) as f:
        lines = f.readlines()
        return lines


def get_signal_strength(code: list[Inst]) -> int:
    vm = SignalStrengthVM()
    vm.execute_code(code)
    return vm.total_signal_strength


def get_display(code: list[Inst]) -> str:
    vm = TubeVM()
    vm.execute_code(code)
    return str(vm)
