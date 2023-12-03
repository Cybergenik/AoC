#!/usr/local/bin/python3

#from functools import lru_cache
#from collections import Counter
from collections import defaultdict


def main():
    print("Herro there")
    with open("input.txt") as f:
        content = f.readlines()
    
    map = defaultdict(lambda: ".")
    numbers = []
    gears = {}
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
            if c == "*":
                gears[(x,y)] = []
        if num_start is not None:
            numbers.append((x, (num_start, num_end), l[num_start:num_end+1]))

    for x, (s, e), numb in numbers:
        print(f'Checking: {numb}, line:{x}, startY:{s}, endY:{e}')
        # handle start and end
        if map[(x, s-1)] == '*':
            gears[(x, s-1)].append(int(numb))
            continue
        if map[(x, e+1)] == '*':
            gears[(x, e+1)].append(int(numb))
            continue
        # handle middle
        for y in range(s-1, e+2):
            if map[(x+1, y)] == '*':
                gears[(x+1, y)].append(int(numb))
            if map[(x-1, y)] == '*':
                gears[(x-1, y)].append(int(numb))
                break 

    total = 0
    for v in gears.values():
        if len(v) == 2:
            total += v[0]*v[1]

    print(total)
if __name__ == "__main__":
    raise SystemExit(main())
