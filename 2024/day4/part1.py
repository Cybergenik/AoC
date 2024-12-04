#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter
import sys
sys.setrecursionlimit(100000)

def adj(x, y, graph):
    yield "".join([graph[(x+1, y)], graph[(x+2, y)], graph[(x+3, y)]])
    yield "".join([graph[(x-1, y)], graph[(x-2, y)], graph[(x-3, y)]])
    yield "".join([graph[(x, y+1)], graph[(x, y+2)], graph[(x, y+3)]])
    yield "".join([graph[(x, y-1)], graph[(x, y-2)], graph[(x, y-3)]])
    yield "".join([graph[(x+1, y+1)], graph[(x+2, y+2)], graph[(x+3, y+3)]])
    yield "".join([graph[(x-1, y-1)], graph[(x-2, y-2)], graph[(x-3, y-3)]])
    yield "".join([graph[(x-1, y+1)], graph[(x-2, y+2)], graph[(x-3, y+3)]])
    yield "".join([graph[(x+1, y-1)], graph[(x+2, y-2)], graph[(x+3, y-3)]])

def find_xmas(graph, x_locs):
    def find_around(w, loc):
        total = 0
        for seg in adj(*loc, graph):
            if seg == "MAS":
                total += 1
        return total
    total = 0
    for x in x_locs:
        total += find_around("X", x)
    return total

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    x_locs = []
    graph = defaultdict(lambda: ".")
    for x, l in enumerate(content):
        for y, c in enumerate(l.strip()):
            if c in "XMAS":
                loc = (x,y)
                graph[loc] = c
                if c == "X":
                    x_locs.append(loc)
    print(find_xmas(graph, x_locs))
        
if __name__ == "__main__":
    raise SystemExit(main())
