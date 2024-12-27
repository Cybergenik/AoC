#!/usr/local/bin/python3

from collections import defaultdict

def main():
    with open("input.txt") as f:
        content = f.readlines()

    graph = defaultdict(lambda: set())
    for l in content:
        l, r = l.strip().split("-")
        graph[l].add(r)
        graph[r].add(l)

    all_nets = set()
    for c, conns in graph.items():
        if c[0] == "t":
            for c1 in conns:
                for c2 in graph[c1]:
                    if c in graph[c2]:
                        all_nets.add(tuple(sorted([c, c1, c2])))
    print(len(all_nets))
    
if __name__ == "__main__":
    raise SystemExit(main())
