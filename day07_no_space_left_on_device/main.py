"""
Solutions for Advent of Code 2022 Day 7 puzzle: "No space left on device"
https://adventofcode.com/2022/day/7

Copyright (C) 2022. Ákos Nagy
https://www.linkedin.com/in/akosnagy350/
"""

from __future__ import annotations
from typing import Callable, Optional

SMALL_DIR_SIZE = 100000
DISK_SIZE = 70000000
UPDATE_SIZE = 30000000


def get_part_1_results_from_file(file_name: str) -> int:
    root = read_fs_from_file(file_name)
    result = [0]
    root.traverse(result, sum_small_dirs)
    return result[0]


def sum_small_dirs(entry: Entry, result):
    if entry.is_dir:
        total_size = entry.get_size(recursive=True)
        if total_size <= SMALL_DIR_SIZE:
            result[0] = result[0] + total_size


def get_part_2_results_from_file(file_name: str) -> int:
    root = read_fs_from_file(file_name)
    result = {
        'disk_free': DISK_SIZE - root.get_size(recursive=True),
        'to_delete_size': root.get_size(recursive=True)
    }
    root.traverse(result, find_dir_to_delete)
    return result['to_delete_size']


def find_dir_to_delete(entry: Entry, result):
    if entry.is_dir:
        total_size = entry.get_size(recursive=True)
        space_after_delete = result['disk_free'] + total_size
        if space_after_delete >= UPDATE_SIZE and total_size < result['to_delete_size']:
            result['to_delete_size'] = total_size


class Entry:
    def __init__(self, name: str = '', parent: Optional[Entry] = None, is_dir: bool = False,
                 size: Optional[int] = None):
        self.children: dict[str, Entry] = {}
        self.is_dir = is_dir
        self.size = size
        self.parent: Entry = parent
        self.name = name
        assert self.is_dir == (self.size is None), f"{name} must be either a directory or a file with correct size"
        assert (self.parent is None) or self.parent.is_dir, "Parent must be a directory"

    def add_file(self, file_name: str, size: int) -> Entry:
        result = Entry(name=file_name, parent=self, is_dir=False, size=size)
        self.children[file_name] = result
        return result

    def add_dir(self, dir_name: str) -> Entry:
        result = Entry(name=dir_name, parent=self, is_dir=True)
        self.children[dir_name] = result
        return result

    def add_from_ls(self, line: str) -> Entry:
        size, name = line.strip().split(' ', maxsplit=2)
        if size == "dir":
            return self.add_dir(name)
        else:
            return self.add_file(name, int(size))

    def get_full_path(self) -> str:
        if self.parent is None:
            return '/'
        else:
            return self.parent.get_full_path() + '/' + self.name

    def get_root(self) -> Entry:
        if self.parent is None:
            return self
        else:
            return self.get_root()

    def resolve(self, name: str, ensure_dir: bool = False):
        if name == "" or name is None:
            return self
        if name == "..":
            assert self.parent is not None, f'{self.get_full_path()} has no parent'
            return self.parent
        if name == "/":
            return self.get_root()
        if "/" in name:
            child, rest = name.split('/', maxsplit=2)
            return self.resolve(child, ensure_dir=True).resolve(rest, ensure_dir)
        assert name in self.children
        result = self.children[name]
        if ensure_dir:
            assert result.is_dir
        return result

    def get_size(self, recursive: bool = False) -> int:
        if self.is_dir:
            result: int = 0
            for entry in self.children.values():
                result += entry.get_size(recursive)
            return result
        else:
            return self.size

    def traverse(self, arg, fn: Callable[[Entry, any], None]):
        fn(self, arg)
        for entry in self.children.values():
            entry.traverse(arg, fn)


def read_fs(lines: list[str]) -> Entry:
    root = Entry(is_dir=True)
    current = root
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if '\n' == line:
            break
        assert line.startswith('$ ')
        parts = line[2:].strip().split(' ')
        cmd = parts[0]
        if cmd == 'cd':
            current = current.resolve(parts[1])
        elif cmd == 'ls':
            while i < len(lines) and not lines[i].startswith('$ '):
                current.add_from_ls(lines[i])
                i += 1
        else:
            assert False
    return root


def read_fs_from_file(file_name: str) -> Entry:
    """
    Opens a text file that contains cd and ls commands and rebuilds the file system tree
    :param file_name: File name that contains commands and responses
    :return: The root directory
    """
    with open(file_name) as f:
        lines = f.readlines()
        return read_fs(lines)
