from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

from string import ascii_letters


def compute(s: str) -> int:
    total_priorities = 0
    lines = s.split('\n')
    common = None
    for idx in range(len(lines) + 1):
        if (idx + 1) % 3 == 0:
            l1, l2, l3 = lines[idx], lines[idx - 1], lines[idx - 2]
        else:
            continue
        for char in l1:
            if char in l2 and char in l3:
                common = char
                break
        if common is None:
            continue
        total_priorities += ascii_letters.find(common) + 1

    return total_priorities



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('vJrwpWtwJgWrhcsFMMfFFhFp', 'p'),
        ('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'L'),
        ('PmmdzqPrVvPwwTWBwg', 'P'),
        ('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'v'),
        ('ttgJtRGJQctTZtZT', 't'),
        ('CrZsJsPPZsGzwwsLwLmpwMDw', 's'),
    )
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
