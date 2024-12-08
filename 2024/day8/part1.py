#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter

def find_antinodes(graph, freqs):
    antinodes = set()
    for f, locs in freqs.items():
        for i, l1 in enumerate(locs[:-1]):
            for l2 in locs[i+1:]:
                diff_x = l2[0]-l1[0]
                diff_y = l2[1]-l1[1]
                a2a = (l1[0]+(diff_x*2), l1[1]+(diff_y*2))
                a2b = (l1[0]-diff_x, l1[1]-diff_y)
                for a in (a2a, a2b):
                    if graph[a] != "#":
                        antinodes.add(a)
    return antinodes

def main():
    with open("input.txt") as f:
        content = f.readlines()

    graph = defaultdict(lambda: "#")
    freqs = defaultdict(lambda: [])
    for y, line in enumerate(content):
        for x, c in enumerate(line.strip()):
            if c != ".":
                freqs[c].append((x,y))
            graph[(x, y)] = c

    print(len(find_antinodes(graph, freqs)))

if __name__ == "__main__":
    raise SystemExit(main())
