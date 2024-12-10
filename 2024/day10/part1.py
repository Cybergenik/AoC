#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter

def adj(graph, x, y):
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if graph[(nx, ny)] != -1 and graph[(nx, ny)]-graph[(x, y)] == 1:
            yield (nx, ny)

def find_paths(graph, starts):
    scores = defaultdict(lambda: 0)
    def dfs(path, seen):
        if path[-1] not in seen:
            seen.add(path[-1])
            if graph[path[-1]] == 9:
                print(path)
                scores[path[0]] += 1
                return
            for v in adj(graph, *path[-1]):
                dfs(path+[v], seen)
    for s in starts:
        dfs([s], set())
    return scores
def main():
    with open("input.txt") as f:
        content = f.readlines()
        
    graph = defaultdict(lambda: -1)
    starts = []
    for y, l in enumerate(content):
        for x, c in enumerate(l.strip()):
            if c == ".":
                continue
            if c == "0":
                starts.append((x,y))
            graph[(x,y)] = int(c)
    paths = find_paths(graph, starts)
    total = 0
    for k, v in paths.items():
        total += v
    print(total)
if __name__ == "__main__":
    raise SystemExit(main())
