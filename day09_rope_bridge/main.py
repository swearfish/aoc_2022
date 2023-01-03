from __future__ import annotations

import math
from typing import Callable


def get_part_1_results_from_file(file_name: str) -> int:
    commands = get_commands_from_file(file_name)
    return get_visited_points(commands, 1)


def get_part_2_results_from_file(file_name: str) -> int:
    commands = get_commands_from_file(file_name)
    return get_visited_points(commands, 9)


class Command:
    def __init__(self, command: str):
        dir, dist = command.strip().split(' ')
        self.direction: str = dir.upper()
        self.distance: int = int(dist)

    def __repr__(self):
        return f'{self.direction} {self.distance}'

    def __str__(self):
        return self.__repr__()


class Rope:
    def __init__(self, name: str, prev: Rope = None):
        self.prev_x = 0
        self.prev_y = 0
        self.x = 0
        self.y = 0
        self.name = name
        self.pred = prev
        self.next: Rope|None = None
        self.visited = {(0,0)}
        self.total_visited = 1
        if prev is not None:
            prev.next = self

    def apply(self, cmd: Command):
        dx = 0
        dy = 0
        if cmd.direction == "R":
            dx = 1
        if cmd.direction == "L":
            dx = -1
        if cmd.direction == "U":
            dy = -1
        if cmd.direction == "D":
            dy = 1
        for i in range(cmd.distance):
            self._move_by(dx, dy)
            if self.next is not None:
                self.next._follow()
        pass

    def _move_by(self, dx: int, dy: int):
        self._move_to(self.x + dx, self.y + dy)

    def _move_to(self, x: int, y: int):
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = x
        self.y = y

    def _follow(self):
        dx = self.x-self.pred.x
        dy = self.y-self.pred.y
        d = math.sqrt(dx*dx+dy*dy)
        if d > 1:
            lim = 0 if d >= 2 else 1
            mx = self._delta(self.x, self.pred.x, lim)
            my = self._delta(self.y, self.pred.y, lim)
            self._move_by(mx, my)
            key = (self.x, self.y)
            if key not in self.visited:
                self.visited.add(key)
                self.total_visited += 1
            if self.next is not None:
                self.next._follow()

    def _delta(self, current, pred, lim) -> int:
        if current < pred - lim:
            return 1
        if current > pred + lim:
            return -1
        return 0

    def __repr__(self):
        return f'{self.name}: {self.x},{self.y} x {self.total_visited}'

    def __str__(self):
        return self.__repr__()


def get_commands_from_file(file_name: str) -> list[Command]:
    with open(file_name) as f:
        lines = f.readlines()
        commands = []
        for line in lines:
            commands.append(Command(line))
        return commands


def get_visited_points(commands: list[Command], length: int) -> int:
    head = Rope("H")
    tail = head
    for i in range(length):
        tail = Rope(f"{i+1}", tail)
    for command in commands:
        head.apply(command)
    return tail.total_visited

