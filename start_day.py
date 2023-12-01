#!/usr/local/bin/python3

import argparse
from io import BufferedWriter
import os
import time
import urllib.error
import urllib.request


def get_input(year: int, day: int) -> str:
    with open('.env') as f:
        contents = f.read()

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    req = urllib.request.Request(url, headers={'Cookie': contents.strip()})
    return urllib.request.urlopen(req).read().decode()

def dir_open(path) -> BufferedWriter:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int)
    parser.add_argument('day', type=int)
    args = parser.parse_args()

    for _ in range(5):
        try:
            print("downloading...")
            s = get_input(args.year, args.day)
        except urllib.error.URLError as e:
            print(f'Failed: not ready yet: {e}')
            time.sleep(1)
        else:
            break
    else:
        raise SystemExit('Timed out after trying a few times')

    with dir_open(f'{args.year}/day{args.day}/input.txt') as f:
        f.write(s)

    print("all done!")

if __name__ == "__main__":
    raise SystemExit(main())
