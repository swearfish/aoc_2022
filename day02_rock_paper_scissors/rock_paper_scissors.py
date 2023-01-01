def get_score_from_file(file_name: str, score_table) -> int:
    with open(file_name) as f:
        lines = f.readlines()
        return get_score(lines, score_table)


SCORE_LOST = 0
SCORE_DRAW = 3
SCORE_WIN = 6

SCORE_ROCK = 1
SCORE_PAPER = 2
SCORE_SCISSORS = 3

SCORE_TABLE = {
    'A': {
        'name': 'rock',
        'X': SCORE_DRAW + SCORE_ROCK,
        'Y': SCORE_WIN + SCORE_PAPER,
        'Z': SCORE_LOST + SCORE_SCISSORS
    },
    'B': {
        'name': 'paper',
        'X': SCORE_LOST + SCORE_ROCK,
        'Y': SCORE_DRAW + SCORE_PAPER,
        'Z': SCORE_WIN + SCORE_SCISSORS
    },
    'C': {
        'name': 'scissors',
        'X': SCORE_WIN + SCORE_ROCK,
        'Y': SCORE_LOST + SCORE_PAPER,
        'Z': SCORE_DRAW + SCORE_SCISSORS
    }
}


SCORE_TABLE_PART_TWO = {
    'A': {
        'name': 'rock',
        'Y': SCORE_DRAW + SCORE_ROCK,
        'Z': SCORE_WIN + SCORE_PAPER,
        'X': SCORE_LOST + SCORE_SCISSORS
    },
    'B': {
        'name': 'paper',
        'X': SCORE_LOST + SCORE_ROCK,
        'Y': SCORE_DRAW + SCORE_PAPER,
        'Z': SCORE_WIN + SCORE_SCISSORS
    },
    'C': {
        'name': 'scissors',
        'Z': SCORE_WIN + SCORE_ROCK,
        'X': SCORE_LOST + SCORE_PAPER,
        'Y': SCORE_DRAW + SCORE_SCISSORS
    }
}


def get_score(lines: list[str], score_table) -> int:
    result = 0
    for line in lines:
        if ' ' not in line:
            break
        opponent, mine = line.strip().split(' ', 2)
        table = score_table[opponent]
        score = table[mine]
        result += score
    return result
