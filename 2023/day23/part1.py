#!/usr/local/bin/python3

from collections import defaultdict
from collections import deque
from copy import copy

def adj(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y+1)
    yield (x, y-1)

def longest_path(start, end, graph):
    q = deque([(start, int(0), set())])
    largest = 0
    while q:
        v, steps, seen = q.popleft()
        if v == end:
            largest = max(largest, steps)
            continue
        if v not in seen:
            seen.add(v)
            if graph[v] == ">":
                q.append(((v[0], v[1]+1), steps+1, seen))
            elif graph[v] == "<":
                q.append(((v[0], v[1]-1), steps+1, seen))
            elif graph[v] == "^":
                q.append(((v[0]-1, v[1]), steps+1, seen))
            elif graph[v] == "v":
                q.append(((v[0]+1, v[1]), steps+1, seen))
            else:
                explore = []
                for u in adj(*v):
                    if graph[u] != "#" and u not in seen:
                        explore.append(u)
                if len(explore) == 1:
                    q.append((explore[0], steps+1, seen))
                else:
                    for u in explore:
                        q.append((u, steps+1, copy(seen)))
    return largest

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    graph = defaultdict(lambda: "#")
    for x, l in enumerate(content):
        for y, c in enumerate(l.strip()):
            graph[(x,y)] = c

    N = len(content)
    M = len(content[0].strip())
    start = (0, 1)
    end = (N-1, M-2)
    print(N, M)
    print(longest_path(start, end, graph))

if __name__ == "__main__":
    raise SystemExit(main())
