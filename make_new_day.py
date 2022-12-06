import pathlib as pl
import subprocess as sp


def main():
    most_recent_day = get_most_recent_day()
    sp.call(shell=True, args=f"cp -r day{most_recent_day:02} day{most_recent_day + 1:02}")
    sp.call(shell=True, args=f"rm day{most_recent_day + 1:02}/part2.py")
    sp.call(shell=True, args=f"cd day{most_recent_day + 1:02}/ && make d")


def get_most_recent_day() -> int:
    most_recent = None
    for item in pl.Path().iterdir():
        if item.is_dir() and not item.name.startswith('.') and not item.name.startswith('_'):
            day_num_str = item.name.split("day")[-1]
            if day_num_str.startswith('0'):
                day_num_str = day_num_str[-1]
            day_num = int(day_num_str)
            if most_recent is None or day_num > most_recent:
                most_recent = day_num
    if most_recent is None:
        raise Exception
    return most_recent


if __name__ == "__main__":
    main()
