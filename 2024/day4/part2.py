#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter

def adj(x, y, graph):
    yield "".join([graph[(x-1, y-1)], "A", graph[(x+1, y+1)]])
    yield "".join([graph[(x-1, y+1)], "A", graph[(x+1, y-1)]])

def find_xmas(graph, a_locs):
    def find_around(loc):
        total = 0
        for seg in adj(*loc, graph):
            if seg == "MAS" or seg == "SAM":
                total += 1
        return total == 2
    total = 0
    for a in a_locs:
        if find_around(a):
            total += 1
    return total

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    a_locs = []
    graph = defaultdict(lambda: ".")
    for x, l in enumerate(content):
        for y, c in enumerate(l.strip()):
            if c in "MAS":
                loc = (x,y)
                graph[loc] = c
                if c == "A":
                    a_locs.append(loc)
    print(find_xmas(graph, a_locs))
        
if __name__ == "__main__":
    raise SystemExit(main())
