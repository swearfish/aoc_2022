def read_input_file(file_name: str) -> list[int]:
    with open(file_name) as f:
        lines = f.readlines()
        return read_input(lines)


def read_input(lines: list[str]) -> list[int]:
    total_calories = 0
    calories_by_elf = []
    for line in lines:
        line = line.strip()
        if 0 == len(line):
            calories_by_elf.append(total_calories)
            total_calories = 0
        else:
            calories = int(line)
            total_calories += calories
    if 0 != total_calories:
        calories_by_elf.append(total_calories)
    return calories_by_elf


def find_max_calories(file_name: str) -> int:
    input = read_input_file(file_name)
    result = max(input)
    return result


def find_top_3_calories(file_name: str) -> int:
    input = read_input_file(file_name)
    input.sort(reverse=True)
    result = sum(input[0:3])
    return result

