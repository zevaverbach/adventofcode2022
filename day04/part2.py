from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

from string import ascii_letters


def compute(s: str):
    counter = 0
    for line in s.split('\n'):
        try:
            first, second = line.split(',')
        except ValueError:
            continue
        start, end = first.split('-')
        enc_start, enc_end = second.split('-')
        start, end, enc_start, enc_end = int(start), int(end), int(enc_start), int(enc_end)
        rg = range(start, end + 1)
        enc_rg = list(range(enc_start, enc_end + 1))
        for i in rg:
            if i in enc_rg:
                counter += 1
                break
    return counter



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('2-8,3-7', 1),
        ('2-6,4-8\n2-8,3-7', 2),
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
