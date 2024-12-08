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
                alocs = [l1, l2]
                a2b = (l1[0]-diff_x, l1[1]-diff_y)
                while graph[a2b] != "#":
                    alocs.append(a2b)
                    a2b = (a2b[0]-diff_x, a2b[1]-diff_y)
                a2a = (l1[0]+(diff_x*2), l1[1]+(diff_y*2))
                while graph[a2a] != "#":
                    alocs.append(a2a)
                    a2a = (a2a[0]+diff_x, a2a[1]+diff_y)
                for a in alocs:
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
