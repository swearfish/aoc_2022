from typing import Callable


SMAL_DIR_SIZE = 100000
DISK_SIZE = 70000000
UPDATE_SIZE = 30000000


def get_part_1_results_from_file(file_name: str) -> int:
    root = read_root_from_file(file_name)
    result = [0]
    root.traverse(result, sum_small_dirs)
    return result[0]


def sum_small_dirs(result, _name: str, _path: str, is_dir: bool, _size: int, total_size: int):
    if is_dir and total_size <= SMAL_DIR_SIZE:
        result[0] = result[0] + total_size


def get_part_2_results_from_file(file_name: str) -> int:
    root = read_root_from_file(file_name)
    result = {
        'disk_size': DISK_SIZE,
        'root': root,
        'disk_free': DISK_SIZE - root.get_size(recursive=True),
        'to_delete_size': root.get_size(recursive=True)
    }
    root.traverse(result, find_dir_to_delete)
    return result['to_delete_size']


def find_dir_to_delete(result, _name: str, _path: str, is_dir: bool, _size: int, total_size: int):
    if is_dir:
        space_after_delete = result['disk_free'] + total_size
        if space_after_delete >= UPDATE_SIZE and total_size < result['to_delete_size']:
            result['to_delete_size'] = total_size


class Entry:
    def __init__(self, name: str = '', parent=None):
        self.dirs: dict[str, Entry] = {}
        self.files: dict[str, int] = {}
        self.parent: Entry = parent
        self.name = name

    def add_file(self, file_name: str, size: int):
        self.files[file_name] = size

    def add_dir(self, dir_name: str):
        self.dirs[dir_name] = Entry(dir_name, self)

    def get_full_path(self):
        if self.parent is None:
            return '/'
        else:
            return self.parent.get_full_path() + '/' + self.name

    def get_root(self):
        if self.parent is None:
            return self
        else:
            return self.get_root()

    def resolve(self, name: str):
        if name == "/":
            return self.get_root()
        if name.startswith('/'):
            return self.get_root().resolve(name[1:])
        if name == "":
            return self
        parts = name.split('/', maxsplit=2)
        child = parts[0]
        rest = parts[1] if len(parts) > 1 else ""
        if child == "..":
            assert self.parent is not None
            return self.parent.resolve(rest)
        assert parts[0] in self.dirs
        return self.dirs[child].resolve(rest)

    def add(self, line: str):
        size, name = line.strip().split(' ', maxsplit=2)
        if size == "dir":
            self.add_dir(name)
        else:
            self.add_file(name, int(size))

    def get_size(self, recursive: bool = False) -> int:
        result = 0
        for file_name in self.files:
            result += self.files[file_name]
        if recursive:
            for dir_name in self.dirs:
                result += self.dirs[dir_name].get_size(recursive)
        return result

    def traverse(self, arg, fn: Callable[[any, str, str, bool, int, int], None]):
        full_path = self.get_full_path()
        fn(arg, self.name, full_path, True, self.get_size(False), self.get_size(True))
        for file_name in self.files:
            fn(arg, file_name, full_path + '/' + file_name, False, self.files[file_name], self.files[file_name])
        for dir_name in self.dirs:
            self.dirs[dir_name].traverse(arg, fn)


def read_entries(lines: list[str]) -> Entry:
    root = Entry()
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
                current.add(lines[i])
                i += 1
        else:
            assert False
    return root


def read_root_from_file(file_name: str) -> Entry:
    with open(file_name) as f:
        lines = f.readlines()
        return read_entries(lines)
