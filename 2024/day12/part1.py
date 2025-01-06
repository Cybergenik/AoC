#!/usr/local/bin/python3

from collections import defaultdict
#from collections import Counter
 
def adj(graph, x, y):
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        yield (nx, ny)

def explore(graph, plants, plant):
    seen = set()
    val = [0]
    def dfs(v):
        if graph[v] != plant:
            val[0] += 1
            return
        if v not in seen:
            all_seen.add(v)
            seen.add(v)
            for u in adj(graph, *v):
                dfs(u)
    total = 0
    all_seen = set()
    for loc in plants[plant]:
        if loc not in all_seen:
            dfs(loc)
            total += val[0] * len(seen)
            val[0] = 0
            seen = set()
    print(f"{plant}: {total}")
    return total

def main():
    with open("input.txt") as f:
        content = f.readlines()

    graph = defaultdict(lambda: "_")
    plants = defaultdict(lambda: [])
    for y, l in enumerate(content):
        for x, c in enumerate(l.strip()):
            graph[(x,y)] = c
            plants[c].append((x,y))

    total = 0
    for plant in plants:
        total += explore(graph, plants, plant)
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())
