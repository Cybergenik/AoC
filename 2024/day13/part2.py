#!/usr/local/bin/python3

from collections import defaultdict
from functools import cache
import math
import sys
from scipy.optimize import linprog


def most_efficient(Ad, Bd, prize):
    cost = [3, 1]
    ABeq = [[Ad[0], Bd[0]], [Ad[1], Bd[1]]]
    Teq = [prize[0], prize[1]]
    opt = linprog(cost, A_eq=ABeq, b_eq=Teq, bounds=(0, None), method='highs')
    if opt.success:
        a = round(opt.x[0], 3)
        b = round(opt.x[1], 3)
        if a.is_integer() and b.is_integer():
            return int(3*a+b)
    return 0

def main():
    with open("input.txt") as f:
        content = f.read()

    D = 10000000000000
    machines = []
    for m in content.split("\n\n"):
        machines.append([])
        for l in m.split("\n"):
            l = l.strip()
            if l.startswith("Button"):
                l, r = l.split(", ")
                x, y = int(l[-2:]), int(r[2:])
                machines[-1].append([x, y])
            elif l.startswith("Prize:"):
                l, r = l.split(", ")
                x, y = D+int(l.split("=")[-1]), D+int(r[2:])
                machines[-1].append([x,y])
    total = 0
    for m in machines:
        min_cost = most_efficient(*m)
        total += min_cost
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())
