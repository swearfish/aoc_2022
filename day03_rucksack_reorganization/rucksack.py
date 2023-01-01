def get_prio(item: str) -> int:
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    if 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27
    raise "Invalid item"


def get_error_sum_from_file(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        return get_error_sum(lines)


def get_badge_sum_from_file(file_name: str) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        return get_badge_prio_sum(lines)


def get_error_sum(input: list[str]) -> int:
    result = 0
    for line in input:
        part_len = len(line.strip()) // 2
        if 0 == part_len:
            break
        part1, part2 = set(line[0: part_len]), set(line[part_len:])
        common = part1.intersection(part2)
        for item in common:
            prio = get_prio(item)
            result += prio
    return result


def get_badge_prio_sum(lines: list[str]) -> int:
    result = 0
    while 3 <= len(lines):
        group = list(map(lambda x: set(x.strip()), lines[0: 3]))
        lines = lines[3:]
        common = set.intersection(*group)
        assert 1 == len(common)
        for item in common:
            prio = get_prio(item)
            result += prio
    return result
