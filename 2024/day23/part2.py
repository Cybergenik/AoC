#!/usr/local/bin/python3

from collections import defaultdict

def find_largest_net(graph):
    def find_set(comps, comp):
        for c in comps:
            if c not in graph[comp]:
                return
        comps.add(comp)
        for c in graph[comp]:
            find_set(comps, c)
    largest = set()
    for c in graph:
        curr_set = set()
        find_set(curr_set, c)
        if len(curr_set) > len(largest):
            largest = curr_set
    return largest

def main():
    with open("input.txt") as f:
        content = f.readlines()

    graph = defaultdict(lambda: set())
    for l in content:
        l, r = l.strip().split("-")
        graph[l].add(r)
        graph[r].add(l)

    print(",".join(sorted(find_largest_net(graph))))
    
if __name__ == "__main__":
    raise SystemExit(main())
