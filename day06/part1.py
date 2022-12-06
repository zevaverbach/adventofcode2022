from __future__ import annotations

from collections import deque
import os.path
import pathlib as pl
import re
import sys
import time
import typing as t
import urllib.error
import urllib.parse
import urllib.request

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str):
    four_window = deque(maxlen=4)
    for idx, char in enumerate(s):
        if char in four_window:
            four_window.clear()
        elif len(four_window) == 3:
            return idx
        four_window.append(char)
    raise Exception('no answer')



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7))
)

#### HELPERS 

def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> None:
    print(compute(pl.Path("input.txt").read_text()))


HERE = os.path.dirname(os.path.abspath(__file__))


def _get_cookie_headers() -> dict[str, str]:
    with open(os.path.join(HERE, '../.env')) as f:
        contents = f.read().strip()
    return {'Cookie': contents}


def get_input(year: int, day: int) -> str:
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    req = urllib.request.Request(url, headers=_get_cookie_headers())
    return urllib.request.urlopen(req).read().decode()


def get_year_day() -> tuple[int, int]:
    cwd = os.getcwd() # type: ignore
    day_s = os.path.basename(cwd)
    year_s = os.path.basename(os.path.dirname(cwd))

    if not day_s.startswith('day') or not year_s.startswith('20'):
        raise AssertionError(f'unexpected working dir: {cwd}')

    return int(year_s), int(day_s[len('day'):])


def download_input() -> int:
    year, day = get_year_day()

    for _ in range(5):
        try:
            s = get_input(year, day)
        except urllib.error.URLError as e:
            print(f'zzz: not ready yet: {e}')
            time.sleep(1)
        else:
            break
    else:
        raise SystemExit('timed out after attempting many times')

    with open('input.txt', 'w') as f:
        f.write(s)
    inputs = s
    if '\n' in inputs.strip():
        print('splitting')
        inputs = inputs.split('\n')
        print(inputs[0])
        if inputs[0].isnumeric():
            print('ints')
            inputs = list(map(int, inputs))
        inputs = str(inputs).replace("'", '"')

    lines = s.splitlines()
    if len(lines) > 10:
        for line in lines[:10]:
            print(line)
        print('...')
    else:
        print(lines[0][:80])
        print('...')

    return 0


TOO_QUICK = re.compile('You gave an answer too recently.*to wait.')
WRONG = re.compile(r"That's not the right answer.*?\.")
RIGHT = "That's the right answer!"
ALREADY_DONE = re.compile(r"You don't seem to be solving.*\?")


def _post_answer(year: int, day: int, part: int, answer: int) -> str:
    params = urllib.parse.urlencode({'level': part, 'answer': answer})
    req = urllib.request.Request(
        f'https://adventofcode.com/{year}/day/{day}/answer',
        method='POST',
        data=params.encode(),
        headers=_get_cookie_headers(),
    )
    resp = urllib.request.urlopen(req)

    return resp.read().decode()


def submit_solution() -> int:
    year, day = get_year_day()
    part = get_part()
    answer = compute(pl.Path("input.txt").read_text())

    print(f'answer: {answer}')

    contents = _post_answer(year=year, day=day, part=part, answer=answer)

    for error_regex in (WRONG, TOO_QUICK, ALREADY_DONE):
        error_match = error_regex.search(contents)
        if error_match:
            print(f'\033[41m{error_match[0]}\033[m')
            return 1

    if RIGHT in contents:
        print(RIGHT)
        return 0
    else:
        # unexpected output?
        print(contents)
        return 1


def get_part() -> t.Literal[1, 2]:
    if __file__.endswith("2.py"):
        return 2
    return 1


if __name__ == '__main__':
    if sys.argv[1] == "get_input":
        print('getting input data...')
        download_input()
    elif sys.argv[1] == "submit":
        submit_solution()
    raise SystemExit(main())
