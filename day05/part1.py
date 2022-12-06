from __future__ import annotations

import argparse
import os.path
import re

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str):
    _stacks = []
    for _ in range(9):
        _stacks.append([])
    stopped_at_idx = None
    for i, line in enumerate(s.split('\n')):
        if not line.strip().startswith("["):
            stopped_at_idx = i
            break
        for idx, char in enumerate(line):
            if char in "[]":
                continue
            elif char != " ":
                if idx == 1:
                    stack_idx = 0
                else:
                    stack_idx = ((idx - 1) // 4) 
                _stacks[stack_idx].append(char)
    stacks = []
    for st in _stacks:
        stacks.append(list(reversed(st)))
    
    if stopped_at_idx is None:
        raise Exception
    for line in s.split('\n'):
        if not line.strip().startswith("move"):
            print(line)
            continue
        match = re.match(r".* ([0-9]+).*([0-9]+).*([0-9]+)", line)
        quantity, fr, t = match[1], match[2], match[3] # type: ignore
        print(quantity, fr, t)
        fr = int(fr) - 1
        t = int(t) - 1
        print(stacks[fr], stacks[t])
        for _ in range(int(quantity)):
            if not stacks[fr]:
                break
            stacks[t].append(stacks[fr].pop())
        print(stacks[fr], stacks[t])
    answer = ''
    for stack in stacks:
        if stack:
            answer += stack[-1]
        else:
            print('appending a blank')
            answer += " "
    return answer



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (("""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""", "CMZ"),
))
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
