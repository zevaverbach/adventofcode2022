from __future__ import annotations

import argparse
import os.path
from collections import deque

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str):
    four_window = deque(maxlen=14)
    for idx, char in enumerate(s):
        if char in four_window:
            four_window.clear()
        elif len(four_window) == 13:
            return idx
        four_window.append(char)
    raise Exception('no answer')



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7))
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
