#!/usr/local/bin/python3

from collections import defaultdict
import sys
from copy import copy
from collections import deque
import heapq
from functools import cache
#from collections import Counter

def print_board(graph, N, M):
    for y in range(M):
        for x in range(N):
            print(graph[(x,y)], end="")
        print("")
    print("")

def adj(graph, x, y, dir):
    if graph[(x, y-1)] != "#" and dir != "v":
        yield (x, y-1), "^"
    if graph[(x, y+1)] != "#" and dir != "^":
        yield (x, y+1), "v"
    if graph[(x-1, y)] != "#" and dir != ">":
        yield (x-1, y), "<"
    if graph[(x+1, y)] != "#" and dir != "<":
        yield (x+1, y), ">"

def shortest_path(graph, s, e, M, N):
    heap = [(0, s, ">")]
    seen = set()
    min_cost = sys.maxsize
    while heap:
        cost, v, dir = heapq.heappop(heap)
        if cost >= min_cost:
            continue
        if v == e:
            min_cost = min(min_cost, cost)
            continue
        if (v, dir) not in seen:
            seen.add((v, dir))
            for u, ndir in adj(graph, *v, dir):
                if dir == ndir:
                    heapq.heappush(heap, (cost+1, u, ndir))
                else:
                    heapq.heappush(heap, (cost+1001, u, ndir))
    return min_cost

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    graph = defaultdict(lambda: "#")
    start = None
    end = None
    M = len(content)
    N = len(content[0].strip())
    for y, l in enumerate(content):
        for x, c in enumerate(l.strip()):
            graph[(x,y)] = c
            if c == "S":
                start = (x,y)
            if c == "E":
                end = (x,y)
    print(shortest_path(graph, start, end, M, N))
if __name__ == "__main__":
    raise SystemExit(main())
