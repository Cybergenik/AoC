#!/usr/local/bin/python3

from collections import defaultdict
from functools import cache
import sys
#from collections import Counter
 
def adj(graph, x, y, N, M):
    if y-1 >= 0 and graph[(x, y-1)] == ".":
        yield (x, y-1)
    if y+1 <= M and graph[(x, y+1)] == ".":
        yield (x, y+1)
    if x-1 >= 0 and graph[(x-1, y)] == ".":
        yield (x-1, y)
    if x+1 <= N and graph[(x+1, y)] == ".":
        yield (x+1, y)

def shortest_path(graph, start, end, N, M):
    work = [(start, 0)]
    seen = set()
    while work:
        v, steps = work.pop(0)
        if v == end:
            return steps
        if v not in seen:
            seen.add(v)
            for u in adj(graph, *v, N, M):
                work.append((u, steps+1))

def print_board(graph, N, M):
    for y in range(M+1):
        for x in range(N+1):
            print(graph[(x,y)], end="")
        print("")
    print("")

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    graph = defaultdict(lambda: '.')
    start = (0, 0)
    N = 70
    M = 70
    end = (N, M)
    bts = []
    for i, l in enumerate(content):
        x, y = l.strip().split(",")
        bts.append((int(x), int(y)))
    
    byte = 1024
    for b in bts[:byte]:
        graph[b] = "#"
    for b in bts[byte:]:
        graph[b] = "#"
        if shortest_path(graph, start, end, N, M) is None:
            print(byte, b)
            break
        byte += 1

if __name__ == "__main__":
    raise SystemExit(main())
