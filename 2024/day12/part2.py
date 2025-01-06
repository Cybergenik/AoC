#!/usr/local/bin/python3

from collections import defaultdict
#from collections import Counter
 
def adj(graph, x, y):
    for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
        yield (x+dx, y+dy), (dx, dy)

def explore(graph, plants, plant, all_seen):
    seen = set()
    edges = set()
    def dfs(v, dir=None):
        if v in all_seen and graph[v] == plant:
            return
        if graph[v] != plant:
            edges.add((v, dir))
            return
        all_seen.add(v)
        seen.add(v)
        for u, dir in adj(graph, *v):
            dfs(u, dir)
    area = 0
    for loc in plants[plant]:
        if loc not in all_seen:
            dfs(loc)
            area += len(seen)
            seen = set()
    all_neighbors = {((u[0]+dir[0], u[1]+dir[1]), dir) for u, dir in edges}
    sides = len(edges-all_neighbors)
    return area*sides

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
    all_seen = set()
    for plant in plants:
        total += explore(graph, plants, plant, all_seen)
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())
