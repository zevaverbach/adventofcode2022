from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    """
    A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

    The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

    The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    score = 0
    me_lu = {"X": 1, "Y": 2, "Z": 3}
    lu = {"A": 1, "B": 2, "C": 3}
    # 2 > 1
    # 3 > 2
    # 1 > 3
    for line in s.split('\n'):
        if line.strip() == "":
            continue
        elf, _, me = line
        score += me_lu[me]
        if me_lu[me] == lu[elf]:
            score += 3
        if me_lu[me] == 1 and lu[elf] == 3:
            score += 6
        elif me_lu[me] == 3 and lu[elf] == 1:
            score += 0
        elif me_lu[me] > lu[elf]:
            score += 6

    return score


INPUT_S = '''\
1000

2000

5000

1000
4001
'''
EXPECTED = 5001


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
