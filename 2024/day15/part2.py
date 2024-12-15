#!/usr/local/bin/python3

from collections import defaultdict
from tqdm import tqdm
#from collections import Counter

def print_board(graph, N, M):
    for y in range(M):
        for x in range(N):
            print(graph[(x,y)], end="")
        print("")
    print("")

def next_move(graph, x, y, dir):
    if dir == "^":
        return (x, y-1), graph[(x, y-1)]
    if dir == "v":
        return (x, y+1), graph[(x, y+1)]
    if dir == ">":
        return (x+1, y), graph[(x+1, y)]
    if dir == "<":
        return (x-1, y), graph[(x-1, y)]

def move(graph, obj, mvs):
    prev = obj
    for dir in mvs:
        to_move = []
        work = [(prev, dir)]
        seen = set()
        valid = True
        while work:
            curr, dir = work.pop(0)
            loc, o = next_move(graph, *curr, dir)
            if curr not in seen:
                seen.add(curr)
                to_move.append((curr, loc))
                if o == "#":
                    valid = False
                    break
                elif o in "[]":
                    work.append((loc, dir))
                    if graph[loc] == "[" and dir in "^v":
                        work.append(((loc[0]+1, loc[1]), dir))
                    elif graph[loc] == "]" and dir in "^v":
                        work.append(((loc[0]-1, loc[1]), dir))
        if valid:
            for s, d in to_move[::-1]:
                graph[d] = graph[s]
                graph[s] = "."
                prev = d

def main():
    with open("input.txt") as f:
        content = f.read()
    
    p1, p2 = content.split("\n\n")
    
    graph = defaultdict(lambda: "#")
    mvs = []
    robot = None
    M = len(p1.split("\n"))
    N = len(p1.split("\n")[0])*2
    for y, l in enumerate(p1.split("\n")):
        for x, c in enumerate(l):
            loc1 = (x*2, y)
            loc2 = (x*2+1, y)
            if c == "@":
                graph[loc1] = c
                graph[loc2] = "."
                robot = loc1
            if c == "O":
                graph[loc1] = "["
                graph[loc2] = "]"
            if c == "#":
                graph[loc1] = c
                graph[loc2] = c
            if c == ".":
                graph[loc1] = c
                graph[loc2] = c

    for l in p2.split("\n"):
        mvs += [c for c in l.strip()]
    
    print(N, M)
    print_board(graph, N, M)
    move(graph, robot, mvs)
    print_board(graph, N, M)
    print(sum((y*100)+x for (x,y) in graph if graph[(x,y)] == "["))

if __name__ == "__main__":
    raise SystemExit(main())
