#!/usr/local/bin/python3

from collections import defaultdict
from functools import cache
import sys
#from collections import Counter
 

def most_efficient(Ad, Bd, prize):
    @cache
    def combos(ap, bp):
        if ap > 100 or bp > 100:
            return sys.maxsize
        x, y = ap*Ad[0], ap*Ad[1] 
        x += bp*Bd[0]
        y += bp*Bd[1] 
        if (x,y) == prize:
            return ap*3 + bp
        if x > prize[0] or y > prize[1]:
            return sys.maxsize
        return min(combos(ap+1, bp), combos(ap, bp+1))
    return combos(0, 0)

def main():
    with open("test.txt") as f:
        content = f.read()

    machines = []
    for m in content.split("\n\n"):
        machines.append([])
        for l in m.split("\n"):
            l = l.strip()
            if l.startswith("Button"):
                l, r = l.split(", ")
                x, y = int(l[-2:]), int(r[2:])
                machines[-1].append((x, y))
            elif l.startswith("Prize:"):
                l, r = l.split(", ")
                x, y = int(l.split("=")[-1]), int(r[2:])
                machines[-1].append((x,y))
    total = 0
    for m in machines:
        print(*m)
        prize = most_efficient(*m)
        total += prize if prize != sys.maxsize else 0
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())
