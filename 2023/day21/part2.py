#!/usr/local/bin/python3

from collections import deque

def adj(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def reachable_steps(start, S, graph, N, M):
    q = deque([(start, 0)])
    final_set = set()
    seen = set()
    while q:
        v, steps = q.popleft()
        if steps == S:
            final_set.add(v)
            continue
        if steps > S:
            continue
        if (v, steps) not in seen:
            seen.add((v, steps))
            for e in adj(*v):
                loc = (e[0] % N, e[1] % M)
                if graph[loc] == "." or graph[loc] == "S":
                    q.append((e, steps+1))
    return len(final_set)

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    start = (0,0)
    graph = {}
    total_valid = 0
    N = len(content)
    M = len(content[0].strip())
    for x, l in enumerate(content):
        for y, c in enumerate(l.strip()):
            graph[(x,y)] = c
            if c == "S":
                start = (x, y)
            if c == ".":
                total_valid += 1

    print(N, M)
    print(start)
    print(total_valid)
    maps_covered = 26501365//total_valid
    total = maps_covered*total_valid
    print(reachable_steps(start, 26501365%total_valid, graph, N, M))

if __name__ == "__main__":
    raise SystemExit(main())
