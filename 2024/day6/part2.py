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

def find_all_obstructions(graph, guard_start, all_locs):
    total = 0
    for x, y in all_locs:
        if graph[(x,y)] == ".":
            graph[(x,y)] = "#"
            curr = (guard_start, "^")
            seen = set()
            while graph[curr[0]] != "_":
                if curr in seen:
                    total += 1
                    break
                seen.add(curr)
                curr = next_step(graph, *curr[0], curr[1])
            graph[(x,y)] = "."
    return total

def walk(graph, guard_start):
    curr = (guard_start, "^")
    seen = set()
    while graph[curr[0]] != "_":
        if curr[0] not in seen:
            seen.add(curr[0])
        curr = next_step(graph, *curr[0], curr[1])
    return seen

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    graph = defaultdict(lambda: "_")
    guard_loc = None
    for y, l in enumerate(content):
        for x, c in enumerate(l.strip()):
            graph[(x,y)] = c
            if c == "^":
                guard_loc = (x,y)
    all_locs = walk(graph, guard_loc)
    all_locs.remove(guard_loc)
    print(find_all_obstructions(graph, guard_loc, all_locs))
    
if __name__ == "__main__":
    raise SystemExit(main())
