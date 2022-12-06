from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

from string import ascii_letters


def compute(s: str) -> int:
    total_priorities = 0
    for line in s.split('\n'):
        print(line)
        c1, c2 = line[:int(len(line) / 2)], line[int(len(line)/2):]
        common = None
        for char in c1:
            if char in c2:
                common = char
                break
        if common is None:
            continue
        total_priorities += ascii_letters.find(common) + 1

    return total_priorities



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('vJrwpWtwJgWrhcsFMMfFFhFp', ascii_letters.find('p') + 1),
        ('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', ascii_letters.find('L') + 1),
        ('PmmdzqPrVvPwwTWBwg', ascii_letters.find('P') + 1),
        ('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', ascii_letters.find('v') + 1),
        ('ttgJtRGJQctTZtZT', ascii_letters.find('t') + 1),
        ('CrZsJsPPZsGzwwsLwLmpwMDw', ascii_letters.find('s') + 1),
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
