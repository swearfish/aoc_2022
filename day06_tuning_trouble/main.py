HEAD_LEN_PART_1 = 4
HEAD_LEN_PART_2 = 14


def get_chars_before_message_in_file(file_name: str, unique: int) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        return get_chars_before_message(lines[0], unique)


def get_chars_before_message(stream: str, unique: int) -> int:
    head = []
    if len(stream) < unique:
        return -1
    for ch in stream[0: unique-1]:
        head.append(ch)
    for index in range(3, len(stream)):
        ch = stream[index]
        head.append(ch)
        head_set = set(head)
        if len(head_set) == unique:
            return index + 1
        head = head[1: ]
    return -1
