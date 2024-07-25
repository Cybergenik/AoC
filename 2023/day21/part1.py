#!/usr/local/bin/python3

from collections import defaultdict
from collections import deque

def adj(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def reachable_steps(start, N, graph):
    q = deque([(start, 0)])
    final_set = set()
    seen = set()
    while q:
        v, steps = q.popleft()
        if steps == N:
            final_set.add(v)
            continue
        elif steps > N:
            continue
        if (v, steps) not in seen:
            seen.add((v, steps))
            for e in adj(*v):
                if graph[e] == "." or graph[e] == "S":
                    q.append((e, steps+1))
    return len(final_set)

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    start = (0,0)
    graph = defaultdict(lambda: "#")
    for x, l in enumerate(content):
        for y, c in enumerate(l.strip()):
            graph[(x,y)] = c
            if c == "S":
                start = (x, y)

    print(reachable_steps(start, 64, graph))

if __name__ == "__main__":
    raise SystemExit(main())
