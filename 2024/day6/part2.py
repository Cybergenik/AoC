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

def find_all_obstructions(graph, guard_start, N, M):
    total = 0
    for x in range(N):
        for y in range(M):
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

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    graph = defaultdict(lambda: "_")
    guard_loc = None
    N = 0
    M = 0
    for y, l in enumerate(content):
        M += 1
        for x, c in enumerate(l.strip()):
            N += 1
            graph[(x,y)] = c
            if c == "^":
                guard_loc = (x,y)
    print(find_all_obstructions(graph, guard_loc, N, M))
    
if __name__ == "__main__":
    raise SystemExit(main())
