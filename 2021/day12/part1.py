#!/usr/local/bin/python3

from collections import defaultdict

def backtrack_sols(graph: dict) -> int:
    def backtrack(v: str, seen: set):
        nonlocal total
        if v == 'end':
            total += 1
            return
        seen.add(v)
        for u in graph[v]:
            if u[0].isupper() or u not in seen:
                backtrack(u, seen)
        seen.discard(v)
    total = 0
    backtrack('start', set())
    return total

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    graph = defaultdict(lambda:[])

    for t in content:
        v, u = t.strip().split('-')
        graph[v].append(u)
        graph[u].append(v)

    print(f'Different paths: {backtrack_sols(graph)}')
    
if __name__ == "__main__":
    raise SystemExit(main())
