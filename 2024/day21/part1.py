#!/usr/local/bin/python3

from collections import deque
from copy import copy
from collections import defaultdict
import sys

def keypad():
    return {
        "A": {
            ">": ["v"],
            "^": ["<"],
            "v": ["v<", "<v"],
            "<": ["v<<", "<<v"],
        },
        "^": {
            ">": ["v>", ">v"],
            "A": [">"],
            "v": ["v"],
            "<": ["v<", "<v"],
        },
        "v": {
            ">": [">"],
            "A": [">^", "^>"],
            "^": ["^"],
            "<": ["<"],
        },
        ">": {
            "v": ["<"],
            "A": ["^"],
            "^": ["<^", "^<"],
            "<": ["<<"],
        },
        "<": {
            "v": [">"],
            "A": [">>^", "^>>"],
            "^": [">^", "^>"],
            ">": [">>"],
        },
    }

def num_pad():
    return [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3],
        [-1, 0, "A"],
    ]

def shortest_keypad(dst, kbds, kp=keypad()):
    if len(robots) == 1:
       return kp[kpds[-1]][dst]
    curr_kpd = kpds.pop(0)
    min_moves = "*"*100
    last_pos = 
    for path in kp[curr_kpd][dst]:
        moves = ""
        for d in path:
            moves += shortest_keypad(d, robots)
        min_moves = min(min_moves, moves)
    return min_moves

def shortest_numpad_sequence(target):
    # human, robot1, robot2, robot3
    work = deque([("A", "A", "A", "A")])
    min_cost = sys.maxsize
    for t in target:
        min_hpath = "*"*100
        while work:
            human, r1, r2, numr3 = work.popleft()
            if numr2 == t:
                min_hpath = min(min_hpath, human)
                continue
            if v == e:
                min_cost = min(min_cost, cost)
                continue
            if v not in seen:
                seen.add(v)
                for u, chts in adj(graph, *v, [0, 0, 0]):
                    work.append((cost+1, u))
    return min_cost

def main():
    with open("test.txt") as f:
        content = f.readlines()
    
    nums = [l.strip() for l in content]
    
if __name__ == "__main__":
    raise SystemExit(main())
