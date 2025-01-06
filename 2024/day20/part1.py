#!/usr/local/bin/python3

from collections import deque
from copy import copy
from collections import defaultdict
import sys

def print_board(graph, N, M):
    for y in range(M):
        for x in range(N):
            print(graph[(x,y)], end="")
        print("")
    print("")

def adj(graph, x, y, cheats):
    if graph[(x, y-1)] != "#":
        yield (x, y-1), False
    elif len(cheats) < 1:
        yield (x, y-1), True

    if graph[(x, y+1)] != "#":
        yield (x, y+1), False
    elif len(cheats) < 1:
        yield (x, y+1), True

    if graph[(x+1, y)] != "#":
        yield (x+1, y), False
    elif len(cheats) < 1:
        yield (x+1, y), True

    if graph[(x-1, y)] != "#":
        yield (x-1, y), False
    elif len(cheats) < 1:
        yield (x-1, y), True

def saved_paths(graph, s, e, sp, N):
    work = deque([(0, s, set(), set())])
    seen_chts = set()
    while work:
        cost, v, cht_seen, seen = work.popleft()
        if cost > sp-N:
            continue
        if v == e:
            if cost == sp-N:
                seen_chts.add(tuple(sorted(cht_seen)))
            continue
        for u, chts in adj(graph, *v, cht_seen):
            cs = copy(cht_seen)
            if chts:
                cs.add(u)
            work.append((cost+1, u, cs, copy(seen)))

    return len(seen_chts)

def shortest_path(graph, s, e):
    work = deque([(0, s)])
    seen = set()
    min_cost = sys.maxsize
    while work:
        cost, v = work.popleft()
        if cost >= min_cost:
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
    with open("input.txt") as f:
        content = f.readlines()
    
    graph = defaultdict(lambda: "#")
    M = len(content)
    N = len(content[0].strip())
    start = None
    end = None
    for y, l in enumerate(content):
        for x, c in enumerate(l.strip()):
            graph[(x,y)] = c
            if c == "S":
                start = (x,y)
            if c == "E":
                end = (x,y)
    shortest = shortest_path(graph, start, end)
    print(shortest)
    print(saved_paths(graph, start, end, shortest, 2))
    
if __name__ == "__main__":
    raise SystemExit(main())
