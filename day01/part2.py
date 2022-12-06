from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    elves_totals = []
    curr = 0
    for c in s.split('\n'):
        if c.strip() == "":
            elves_totals.append(curr)
            curr = 0
        else:
            curr += int(c)
    sor = sorted(elves_totals)
    return sor[-3] + sor[-2] + sor[-1]


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
