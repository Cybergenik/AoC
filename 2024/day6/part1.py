#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter

dirs = {
    "^": (0, -1),
    "v": (0, +1),
    ">": (+1, 0),
    "<": (-1, 0),
}

def next_step(graph, x, y, dir):
    dx, dy = dirs[dir]
    nx, ny = x+dx, y+dy
    if graph[(nx, ny)] == "#":
        if dir == "^":
            return next_step(graph, x, y, ">")
        if dir == ">":
            return next_step(graph, x, y, "v")
        if dir == "v":
            return next_step(graph, x, y, "<")
        if dir == "<":
            return next_step(graph, x, y, "^")
    return ((nx, ny), dir)

def walk(graph, guard_start):
    curr = (guard_start, "^")
    seen = set()
    while graph[curr[0]] != "_":
        if curr[0] not in seen:
            seen.add(curr[0])
        curr = next_step(graph, *curr[0], curr[1])
    return len(seen)

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    map = defaultdict(lambda: "_")
    guard_loc = None
    for y, l in enumerate(content):
        for x, c in enumerate(l.strip()):
            map[(x,y)] = c
            if c == "^":
                guard_loc = (x,y)
    print(walk(map, guard_loc))
    
if __name__ == "__main__":
    raise SystemExit(main())
