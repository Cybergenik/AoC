#!/usr/local/bin/python3

#from functools import lru_cache
#from collections import Counter
from collections import defaultdict


def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    map = defaultdict(lambda: ".")
    numbers = []
    for x, l in enumerate(content):
        l = l.strip()
        num_start = None
        num_end = None
        for y, c in enumerate(l):
            if c.isnumeric():
                if num_start is None:
                    num_start = y
                num_end = y
            else:
                if num_start is not None:
                    numbers.append((x, (num_start, num_end), l[num_start:num_end+1]))
                    num_start = None
                    num_end = None
            map[(x, y)] = c
        if num_end is not None:
            numbers.append((x, (num_start, num_end), l[num_start:num_end+1]))

    total = 0
    for x, (s, e), numb in numbers:
        # handle start and end
        if map[(x, s-1)] != '.' or map[(x, e+1)] != '.':
            total += int(numb)
            continue
        # handle middle
        for y in range(s-1, e+2):
            if map[(x+1, y)] != '.' or map[(x-1, y)] != '.':
                total += int(numb)
                break 

    print(total)
if __name__ == "__main__":
    raise SystemExit(main())
